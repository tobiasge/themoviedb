try:
    from themoviedb.tmdb import TMDb
except ModuleNotFoundError:
    pass
try:
    from themoviedb.aiotmdb import aioTMDb
except ModuleNotFoundError:
    pass
