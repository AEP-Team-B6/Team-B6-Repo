from __future__ import annotations

import model
from data_access.base_data_access import BaseDataAccess


class FacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)