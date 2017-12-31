import 'common/less/gallery.less';
import moment from 'moment';
import 'bootstrap';
// Polyfills
import 'es6-promise/auto';
import 'whatwg-fetch';
import 'picturefill';

import React from 'react';
import ReactDom from 'react-dom';
import { AppContainer } from 'react-hot-loader';

import { timeOutAlerts } from 'common/utils/';
import HeaderContainer from './header/containers/HeaderContainer';

import { initGoogleMaps } from './maps';
import init from './init';
import './less/core.less';

moment.locale('nb');

initGoogleMaps();
init();
timeOutAlerts();

const renderHeader = (Header) => {
  ReactDom.render(
    <AppContainer>
      <Header />
    </AppContainer>,
    document.getElementById('header'),
  );
};

renderHeader(HeaderContainer);

if (module.hot) {
  module.hot.accept('./header/containers/HeaderContainer', () => {
    renderHeader(HeaderContainer);
  });
}
