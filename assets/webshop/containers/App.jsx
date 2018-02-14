import React from 'react';
import { Router, Route, Switch } from 'react-router';
import moment from 'moment';
import createBrowserHistory from 'history/createBrowserHistory';
import ArticleList from './ArticleList';

const history = createBrowserHistory();

class App extends React.Component {
  constructor() {
    super();
  }

  render() {
    return (
        <Router history={history}>
          <Switch>
            <Route
              exact
              path="/webshop/"
            />
          </Switch>
        </Router>
    );
  }
}

export default App;
