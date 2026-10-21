from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict, Field


router = APIRouter(tags=["experiments"])


class ExperimentSubmission(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    config: dict[str, Any]


@router.post("/experiments")
def submit_experiment(experiment: ExperimentSubmission) -> dict[str, Any]:
    return {
        "status": "validated",
        "saved": False,
        "experiment": experiment.model_dump(),
    }
