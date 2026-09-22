import os
from langchain.chat_models import init_chat_model


model = init_chat_model(
    "ollama:gemma4:e2b",
    temperature=0.7,
)
# response = model.invoke("Why do parrots talk?")
# print(response.content)



# for chunk in model.stream("Why do parrots have colorful feathers?"):
#     print(chunk.text, end="", flush=True)



# responses = model.batch([
#     "Why do parrots have colorful feathers?",
#     "How do airplanes fly?",
#     "What is quantum computing?"
# ])
# for response in responses:
#     print(response.content)
#     print("=" * 40)




# from pydantic import BaseModel, Field

# class Movie(BaseModel):
#     """A movie with details."""
#     title: str = Field(description="The title of the movie")
#     year: int = Field(description="The year the movie was released")
#     director: str = Field(description="The director of the movie")
#     rating: float = Field(description="The movie's rating out of 10")

# model_with_structure = model.with_structured_output(Movie)
# response = model_with_structure.invoke("Provide details about the movie Inception")
# print(response)  # Movie(title="Inception", year=2010, director="Christopher Nolan", rating=8.8)




from langchain.rate_limiters import InMemoryRateLimiter

rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.1,  # 1 request every 10s
    check_every_n_seconds=0.1,  # Check every 100ms whether allowed to make a request
    max_bucket_size=10,  # Controls the maximum burst size.
)

model = init_chat_model(
    model="ollama:gemma4:e2b",
    rate_limiter=rate_limiter  
)


for i in range(15):
    response = model.invoke(f"Request {i+1}: Why do parrots have colorful feathers?")
    print(response.content)


