# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/archetypes/capsules3d.fbs".

# You can extend this class by creating a "Capsules3DExt" class in "capsules3d_ext.py".

from __future__ import annotations

from attrs import define, field

from .. import components
from .._baseclasses import (
    Archetype,
)
from .capsules3d_ext import Capsules3DExt

__all__ = ["Capsules3D"]


@define(str=False, repr=False, init=False)
class Capsules3D(Capsules3DExt, Archetype):
    """
    **Archetype**: 3D capsules; cylinders with hemispherical caps.

    Capsules are defined by two endpoints (the centers of their end cap spheres), which are located
    at (0, 0, 0) and (0, 0, length), that is, extending along the positive direction of the Z axis.
    Capsules in other orientations may be produced by applying a rotation to the entity or
    instances.
    """

    # __init__ can be found in capsules3d_ext.py

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            lengths=None,  # type: ignore[arg-type]
            radii=None,  # type: ignore[arg-type]
            translations=None,  # type: ignore[arg-type]
            rotation_axis_angles=None,  # type: ignore[arg-type]
            quaternions=None,  # type: ignore[arg-type]
            colors=None,  # type: ignore[arg-type]
            labels=None,  # type: ignore[arg-type]
            show_labels=None,  # type: ignore[arg-type]
            class_ids=None,  # type: ignore[arg-type]
        )

    @classmethod
    def _clear(cls) -> Capsules3D:
        """Produce an empty Capsules3D, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    lengths: components.LengthBatch = field(
        metadata={"component": "required"},
        converter=components.LengthBatch._required,  # type: ignore[misc]
    )
    # The shape of the capsule defined as the length of the line between its endpoints.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    radii: components.RadiusBatch = field(
        metadata={"component": "required"},
        converter=components.RadiusBatch._required,  # type: ignore[misc]
    )
    # Radius of the capsules.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    translations: components.PoseTranslation3DBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.PoseTranslation3DBatch._optional,  # type: ignore[misc]
    )
    # Optional translations of the capsules.
    #
    # If not specified, one end of each capsule will be at (0, 0, 0).
    # Note that this uses a [`components.PoseTranslation3D`][rerun.components.PoseTranslation3D] which is also used by [`archetypes.InstancePoses3D`][rerun.archetypes.InstancePoses3D].
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    rotation_axis_angles: components.PoseRotationAxisAngleBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.PoseRotationAxisAngleBatch._optional,  # type: ignore[misc]
    )
    # Rotations via axis + angle.
    #
    # If no rotation is specified, the capsules align with the +Z axis of the local coordinate system.
    # Note that this uses a [`components.PoseRotationAxisAngle`][rerun.components.PoseRotationAxisAngle] which is also used by [`archetypes.InstancePoses3D`][rerun.archetypes.InstancePoses3D].
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    quaternions: components.PoseRotationQuatBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.PoseRotationQuatBatch._optional,  # type: ignore[misc]
    )
    # Rotations via quaternion.
    #
    # If no rotation is specified, the capsules align with the +Z axis of the local coordinate system.
    # Note that this uses a [`components.PoseRotationQuat`][rerun.components.PoseRotationQuat] which is also used by [`archetypes.InstancePoses3D`][rerun.archetypes.InstancePoses3D].
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    colors: components.ColorBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ColorBatch._optional,  # type: ignore[misc]
    )
    # Optional colors for the capsules.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    labels: components.TextBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.TextBatch._optional,  # type: ignore[misc]
    )
    # Optional text labels for the capsules, which will be located at their centers.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    show_labels: components.ShowLabelsBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ShowLabelsBatch._optional,  # type: ignore[misc]
    )
    # Optional choice of whether the text labels should be shown by default.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    class_ids: components.ClassIdBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=components.ClassIdBatch._optional,  # type: ignore[misc]
    )
    # Optional class ID for the ellipsoids.
    #
    # The class ID provides colors and labels if not specified explicitly.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__  # type: ignore[assignment]
