from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas.geometry import Frame
from compas.geometry import Point
from compas.geometry import Vector


def offset_frame(frame, distance):
    new_origin = frame.point + frame.normal * distance

    return Frame(new_origin, frame.xaxis, frame.yaxis)


def ensure_frame(framelike):
    """Convert plane to frame if necessary.

    Parameters
    ----------
    framelike : :class:`Rhino.Geometry.Plane` or :class:`compas.geometry.Frame`
        Framelike or frame object.

    Returns
    -------
    :class:`compas.geometry.Frame`

    Raises
    ------
    :exc:`AttributeError`
        If neither Frame nor Plane.
    """
    if isinstance(framelike, Frame):
        return framelike

    return rgplane_to_cgframe(framelike)


def rgplane_to_cgframe(plane):
    # type: (Rhino.Geometry.Plane) -> compas.geometry.Frame
    """Convert :class:`Rhino.Geometry.Plane` to :class:`compas.geometry.Frame`.

    Parameters
    ----------
    plane : :class:`Rhino.Geometry.Plane`
        Plane object to convert

    Returns
    -------
    :class:`compas.geometry.Frame`
        Resulting frame object
    """
    pt = Point(plane.Origin.X, plane.Origin.Y, plane.Origin.Z)
    xaxis = Vector(plane.XAxis.X, plane.XAxis.Y, plane.XAxis.Z)
    yaxis = Vector(plane.YAxis.X, plane.YAxis.Y, plane.YAxis.Z)
    return Frame(pt, xaxis, yaxis)
