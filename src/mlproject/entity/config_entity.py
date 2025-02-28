from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    sorce_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    STATUS_FILE_2: str
    unzip_data_dir: Path
    all_schema: dict