import cheetah
from pmd_beamphysics import ParticleGroup

def particlegroup_to_cheetah_beam(pg: ParticleGroup):
    """Convert an openPMD-beamphysics ParticleGroup to a Cheetah ParticleBeam."""
    return cheetah.ParticleBeam.from_openpmd_particlegroup(pg)