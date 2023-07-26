/** @odoo-module **/

import { NavBar } from "@web/webclient/navbar/navbar";
import { patch } from 'web.utils';
const { hooks,useState } = owl;
import {useExternalListener, useRef} from "@web/core/utils/hooks";
// const { useExternalListener, useRef, useState } = owl.hooks;
import { bus } from 'web.core';

const config = require('web.config');

patch(NavBar.prototype, 'openeducat_backend_theme/static/src/js/edu/apps_menu.js', {
    setup() {
        this._super();
        this.state = useState({
            is_home_menu: false,
            isMobile: config.device.isMobile,
            prev_url: null,
        });
        bus.on("home_menu_change", this, (res) => {
            this.state.is_home_menu = res;
            this.isMobile = config.device.isMobile;
        });
        bus.on("set_prev_url", this, (res) => {
            this.state.prev_url = res;
        });
    },

    async onClickMainMenu(e) {
        //await $.bbq.pushState('#home=apps', 2);
        this.env.bus.trigger('home_menu_toggled', true);
    },

    async onClickBackButton(e) {
        await $.bbq.pushState(this.state.prev_url, 2);
        this.state.is_home_menu = false;
        this.isMobile = config.device.isMobile;
    },

});