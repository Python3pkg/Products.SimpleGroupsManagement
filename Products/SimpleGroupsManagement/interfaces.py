# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface
from . import messageFactory as _


class ISimpleGroupManagementLayer(Interface):
    """Marker interface for Simple Groups Management product layer
    """


class ISimpleGroupManagementSettings(Interface):
    """Settings used in the control panel for simple group management
    """

    sgm_data = schema.Tuple(
        title=_("Groups management proxy"),
        description=_(
            "help_sgm_data",
            default="Configure which users or groups can manage which groups.\n"
                    "Fill the field below by providing a set of \"user_foo_id|group_bar_id\""
                    " (or \"group_foo_id|group_bar_id\"), one per line.\n"
                    "That means: the user/group on the left of the \"|\" can handle"
                    " group on the right."
        ),
        required=False,
        value_type=schema.TextLine(),
        default=(),
        missing_value=(),
    )

    sgm_never_managed_groups = schema.Tuple(
        title=_("Not manageable groups"),
        description=_(
            "help_gm_never_managed_groups",
            default="Put here a list of groups that can't be managed by users"
        ),
        required=False,
        value_type=schema.TextLine(),
        default=(
            'Administrators',
            'Site Administrators',
            'Reviewers',
            'AuthenticatedUsers',
        ),
        missing_value=(),
    )
