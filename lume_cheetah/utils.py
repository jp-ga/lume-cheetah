import cheetah
from pmd_beamphysics import ParticleGroup
import torch

def particlegroup_to_cheetah_beam(
    pg: ParticleGroup,
    dtype: torch.dtype = torch.float32,
    device: torch.device | str | None = None,
):
    """Convert an openPMD-beamphysics ParticleGroup to a Cheetah ParticleBeam."""
    energy = torch.as_tensor(pg["energy"], dtype=dtype, device=device).mean()

    return cheetah.ParticleBeam.from_openpmd_particlegroup(
        particle_group=pg,
        energy=energy,
        dtype=dtype,
        device=device,
    )