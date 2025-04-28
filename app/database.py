from sqlmodel import Field, Session, SQLModel, create_engine, select

"""
    Home for database setup code and database model definitions
"""

class Movie(SQLModel, table=True):
    id: int = Field(primary_key=True)
    tconst: str | None = Field(default=None)
    primarytitle: str | None = Field(default=None)
    startyear: int | None = Field(default=None)
    rank: int | None = Field(default=None)
    averagerating: float | None = Field(default=None)
    numvotes: int | None = Field(default=None)
    runtimeminutes: int | None = Field(default=None)
    directors: str | None = Field(default=None)
    writers: str | None = Field(default=None)
    genres: str | None = Field(default=None)
    imdblink: str | None = Field(default=None)
    title_imdb_link: str | None = Field(default=None)


sqlite_file_name = 'movies.db'
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
