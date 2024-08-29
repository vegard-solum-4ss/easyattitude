import numpy as np


class Attitude:
    """
    Attitude.

    The primary attitude representation is a direction cosine matrix (DCM), denoted C,
    that rotates vectors from the 'body frame' to the 'NED frame':

    v_ned = C @ v_body

    Parameters
    ----------
    dcm : NDArray
        A 3x3 direction cosine matrix representing the attitude. Rotates vectors from
        the 'body frame' to the 'NED frame'.
    """

    def __init__(self, dcm):
        self._dcm = np.asarray_chkfinite(dcm).reshape(3, 3).copy()

    @classmethod
    def from_quat(cls, quat):
        """
        Create an Attitude from a unit quaternion.

        Parameters
        ----------
        quat : NDArray
            A 4-element unit quaternion.

        Returns
        -------
        Attitude
            Attitude object.
        """
        q = np.asarray_chkfinite(quat).reshape(4)
        eta, *eps = q

    @property
    def dcm(self):
        """
        Attitude as direction cosine matrix (i.e., rotation matrix from-body-to-ned).
        """
        return self._dcm.copy()

    @property
    def euler(self):
        """
        Attitude as Euler angles (i.e., roll, pitch, yaw).
        """
        raise NotImplementedError("Not implemented yet.")

    @property
    def quat(self):
        """
        Attitude as quaternion.
        """
        raise NotImplementedError("Not implemented yet.")

    @property
    def axis_angle(self):
        """
        Attitude as axis-angle representation.
        """
        raise NotImplementedError("Not implemented yet.")

    @property
    def rot_vec(self):
        """
        Attitude as rotation vector.
        """
        raise NotImplementedError("Not implemented yet.")

    @property
    def gibbs(self):
        """
        Attitude as Gibbs vector.
        """
        raise NotImplementedError("Not implemented yet.")
