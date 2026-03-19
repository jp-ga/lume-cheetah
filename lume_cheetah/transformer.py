from abc import ABC, abstractmethod


class CheetahTransformer(ABC):
    """
    Class that handles transformations between control system
    names and values and cheetah element names and attributes.

    Should be subclassed for each specific accelerator facility to handle
    any necessary unit conversions or special cases in the mapping
    between control variables and cheetah properties.

    """
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


