"""原始业务凭据的可读性和关系完整性。"""
import json
from pathlib import Path
import unittest

DATA = Path(__file__).resolve().parents[1] / "data"


def table(name):
    with (DATA / (name + ".json")).open(encoding="utf-8") as stream:
        return json.load(stream)


class SourceDataTest(unittest.TestCase):
def test_return_and_rebate_preserve_original_references(self):
        terminal = {r["id"]:r for r in table("sell_records")}
        for row in terminal.values():
            if row["original"]:
                self.assertEqual(row["batch"], terminal[row["original"]]["batch"])
        for row in table("payments"):
            self.assertIn(row["terminal_id"], terminal)
        sites = {r["site"] for r in table("agreements")}
        transfer = next(r for r in table("movements") if r["movement"]=="T1")
        self.assertEqual(set(transfer["possible_destinations"]), sites-{transfer["from_site"]})

    def test_physical_starting_inventory_and_pending_arrivals(self):
        units = table("supply")["packs"]
        transfer = next(r for r in table("movements") if r["movement"]=="T1")
        opening = next(r for r in table("inventory") if r["state"]=="确认" and r["site"]=="东区")
        self.assertGreater(opening["count"], transfer["quantity"] * units[transfer["unit"]])
        self.assertIn("缺报", {r["state"] for r in table("inventory")})
