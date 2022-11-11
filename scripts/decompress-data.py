from filesplit.merge import Merge
import zipfile
from pathlib import Path
import shutil


raw = Path(".") / "data" / "raw"

print("Merging parts")
m = Merge(
    (raw / "compressed").as_posix(),
    raw.as_posix(),
    "raw.zip"
).merge()

print("Decompressing zip")
with zipfile.ZipFile((raw / "raw.zip").as_posix(), "r") as f:
    f.extractall(raw.as_posix())

print("Cleaning up")
shutil.rmtree((raw / "compressed").as_posix())
(raw / "raw.zip").unlink()
print("Done")
