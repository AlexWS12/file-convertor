from .md_html import md_to_html
from .html_md import html_to_md
from .csv_json import csv_to_json
from .json_csv import json_to_csv
from .csv_npy import csv_to_npy
from .npy_csv import npy_to_csv

CONVERSIONS = {
    (".md", ".html"): md_to_html,
    (".html", ".md"): html_to_md,

    (".csv", ".json"): csv_to_json,
    (".json", ".csv"): json_to_csv,

    (".csv", ".npy"): csv_to_npy,
    (".npy", ".csv"): npy_to_csv,
}
