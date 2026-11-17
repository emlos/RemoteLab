from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict, Field
from app.database import save_experiment, get_experiment, update_experiment, delete_experiment
from fastapi import HTTPException

router = APIRouter(tags=["experiments"])


class ExperimentSubmission(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    config: dict[str, Any]


@router.post("/experiments")
def submit_experiment(experiment: ExperimentSubmission) -> dict[str, Any]:
    try:
        experiment_id = save_experiment(experiment.name, experiment.config)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to save experiment",
        )

    return {
        "status": "saved",
        "id": experiment_id,
    }

@router.get("/experiments")
def read_experiment() -> list[dict[str, Any]]:
    try:
        return get_experiment()
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to read experiment",
        )

@router.put("/experiments/{experiment_id}")
def edit_experiment(experiment_id: int, experiment: ExperimentSubmission) -> dict[str, Any]:
    try:
        updated = update_experiment(
            experiment_id,
            experiment.name,
            experiment.config,
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to update experiment",
        )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Experiment not found",
        )

    return {"status": "updated"}

@router.delete("/experiments/{experiment_id}")
def remove_experiment(experiment_id: int) -> dict[str, Any]:
    try:
        deleted = delete_experiment(experiment_id)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Failed to delete experiment",
        )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Experiment not found",
        )

    return {"status": "deleted"}