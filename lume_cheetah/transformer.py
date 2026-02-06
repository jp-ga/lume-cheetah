from abc import ABC, abstractmethod


class CheetahTransformer(ABC):
    """
    Class that handles transformations between control system
    names and values and cheetah element names and attributes.

    Should be subclassed for each specific accelerator facility to handle
    any necessary unit conversions or special cases in the mapping
    between control variables and cheetah properties.

    Attributes
    ----------
    control_name_to_cheetah: dict[str, str]
        Mapping between control variable names and cheetah element names + attributes.
        Example: {"QUAD:Q1:B1_GRAD": "Q1 k1"}

    """

    def __init__(self, control_name_to_cheetah: dict[str, str]):
        self.control_name_to_cheetah = control_name_to_cheetah

    @property
    def control_name_to_cheetah(self):
        return self._control_name_to_cheetah

    @abstractmethod
    def get_cheetah_property(self, simulator, control_name):
        """
        Given a control variable name, return the corresponding cheetah value.

        Parameters
        ----------
        control_name : str
            The name of the control variable (e.g. "QUAD:Q1:B1_GRAD")

        Returns
        -------
        Any
            The corresponding cheetah element property value
        """
        pass

    @abstractmethod
    def set_cheetah_property(self, simulator, control_name, value):
        """
        Given a control name and value, set the corresponding cheetah property.

        Parameters
        ----------
        control_name : str
            The name of the control variable (e.g. "QUAD:Q1:B1_GRAD")
        value : Any
            The value to set for the corresponding cheetah property
        """
        pass


class SLACCheetahTransformer(CheetahTransformer):
    """
    CheetahTransformer subclass for SLAC accelerator simulations.

    This class can be extended to include any necessary unit conversions or
    special handling for SLAC-specific control variables and their mapping
    to cheetah properties.
    """

    def get_cheetah_property(self, simulator, control_name):
        # Example implementation - this should be customized based on actual mappings
        cheetah_mapping = self.control_name_to_cheetah.get(control_name)
        if cheetah_mapping is None:
            raise ValueError(f"No mapping found for control variable '{control_name}'")
        element_name, attribute = cheetah_mapping.split()
        element = getattr(simulator.segment, element_name)
        return getattr(element, attribute)

    def set_cheetah_property(self, simulator, control_name, value):
        # Example implementation - this should be customized based on actual mappings
        cheetah_mapping = self.control_name_to_cheetah.get(control_name)
        if cheetah_mapping is None:
            raise ValueError(f"No mapping found for control variable '{control_name}'")
        element_name, attribute = cheetah_mapping.split()

        
        element = getattr(simulator.segment, element_name)
        setattr(element, attribute, value)
