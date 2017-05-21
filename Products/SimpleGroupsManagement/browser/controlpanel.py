# -*- coding: utf-8 -*-

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFPlone import PloneMessageFactory as pmf
from Products.SimpleGroupsManagement import messageFactory as _
from Products.SimpleGroupsManagement.interfaces import ISimpleGroupManagementSettings  # noqa
from plone.app.registry.browser import controlpanel
from z3c.form import button


def fix_widget_style(widget):
    widget.style = 'width: 100%'
    widget.klass += " autoresize"
    widget.rows = 7


class SGMSettingsEditForm(controlpanel.RegistryEditForm):
    """Media settings form.
    """
    schema = ISimpleGroupManagementSettings
    id = "SGMSettingsEditForm"
    label = _("Groups management proxy settings")
    description = _(
        "help_sgm_settings_editform",
        default="Configure groups management proxy"  # noqa
    )

    @button.buttonAndHandler(pmf('Save'), name='save')
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        changes = self.applyChanges(data)
        IStatusMessage(self.request).addStatusMessage(_("Changes saved"),
                                                      "info")
        self.context.REQUEST.RESPONSE.redirect(
            "@@configure-simple-groups-management"
        )

    @button.buttonAndHandler(pmf('Cancel'), name='cancel')
    def handleCancel(self, action):
        IStatusMessage(self.request).addStatusMessage(_("Edit cancelled"),
                                                      "info")
        self.request.response.redirect("%s/%s" % (self.context.absolute_url(),
                                                  self.control_panel_view))

    def updateWidgets(self):
        super(SGMSettingsEditForm, self).updateWidgets()
        fix_widget_style(self.widgets['sgm_data'])
        fix_widget_style(self.widgets['sgm_never_managed_groups'])


class SGMSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    """SGM settings control panel.
    """
    form = SGMSettingsEditForm
    # index = ViewPageTemplateFile('controlpanel.pt')
