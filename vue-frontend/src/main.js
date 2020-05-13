import Vue from "vue";
import App from "./App.vue";
import VueFileAgent from "vue-file-agent";
import VueFileAgentStyles from "vue-file-agent/dist/vue-file-agent.css";
import vuetify from "./plugins/vuetify";

Vue.use(VueFileAgent);
Vue.use(VueFileAgentStyles);
Vue.config.productionTip = false;

new Vue({
  vuetify,
  render: h => h(App)
}).$mount("#app");
