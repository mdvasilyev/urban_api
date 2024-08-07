from sqlalchemy import Column, ForeignKey, Integer, Sequence, Table, Text, text
from geoalchemy2.types import Geometry
from urban_api.db import metadata
from sqlalchemy.dialects.postgresql import JSONB

project_territory_id_seq = Sequence("project_territory_id_seq", schema="user_projects_unmanaged")

projects_territory_data = Table(
    "projects_territory_data",
    metadata,
    Column("project_territory_id", Integer, primary_key=True, server_default=project_territory_id_seq.next_value()),
    Column(
        "parent_id",
        Integer,
        ForeignKey("user_projects_unmanaged.projects_territory_data.project_territory_id"),
        nullable=True,
    ),
    Column(
        "geometry",
        Geometry(spatial_index=False, from_text="ST_GeomFromEWKT", name="geometry"),
        nullable=False,
    ),
    Column(
        "centre_point",
        Geometry("POINT", spatial_index=False, from_text="ST_GeomFromEWKT", name="geometry"),
        nullable=False,
    ),
    Column("properties", JSONB(astext_type=Text()), nullable=False, server_default=text("'{}'::jsonb")),
    schema="user_projects_unmanaged",
)

"""
Project territory data:
- project_territory_id int 
- parent_id foreign key int
- geometry geometry
- centre_point geometry point
- properties jsonb
"""
