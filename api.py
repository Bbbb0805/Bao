
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# -------data--------
class Film(BaseModel):
    show_id: int
    cast: str
    country: str
    date_added: str
    description: str
    director: str
    duration: str
    listed_in: str
    rating: str
    release_year: str
    title: str
    type: str


films = [
    {'show_id': 0,
     'cast': 'A Fire Upon the Deep 1',
     'country': 'Vernor Vinge',
     'date_added': 'The coldsleep itself was dreamless.',
     'description': '1992',
     'director': '1992',
     'duration': '1992',
     'listed_in': '1992',
     'rating': '1992',
     'release_year': '1992',
     'title': '1992',
     },
    {'show_id': 1,
     'cast': 'A Fire Upon the Deep 2',
     'country': 'Vernor Vinge',
     'date_added': 'The coldsleep itself was dreamless.',
     'description': '1992',
     'director': '1992',
     'duration': '1992',
     'listed_in': '1992',
     'rating': '1992',
     'release_year': '1992',
     'title': '1992',
     }
]


# -------Get data----------
@app.get("/")
async def home():
    results = []
    for film in films:
        results.append(film)
    return results

