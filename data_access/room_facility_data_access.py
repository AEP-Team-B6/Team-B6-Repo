from __future__ import annotations

from data_access.base_data_access import BaseDataAccess


class RoomFacilityDataAccess(BaseDataAccess):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)


    # Used in User Story 9
    def get_facility_ids_by_room(self, room_id: int) -> list[int]:

        sql = """
        SELECT facility_id FROM Room_Facilities WHERE room_id = ?
        """

        params = tuple([room_id])
        result = self.fetchall(sql, params)
        return [row[0] for row in result]