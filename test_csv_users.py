import os
import csv

def test_csv_file_exists():
    assert os.path.exists("/Users/homemacbook/Desktop/every_5th_user.csv"), "❌ CSV-файл не знайдено"

def test_csv_rows_content():
    with open("/Users/homemacbook/Desktop/every_5th_user.csv", mode="r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) > 0, "❌ CSV-файл порожній"
        assert "name" in rows[0], "❌ У файлі немає поля 'name'"

