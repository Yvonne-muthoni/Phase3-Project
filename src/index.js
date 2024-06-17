import React from 'react';
import { createRoot } from 'react-dom/client';
import { BrowserRouter } from 'react-router-dom';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
import '../node_modules/bootstrap/dist/js/bootstrap.bundle';
import 'font-awesome/css/font-awesome.min.css';
import './index.css';
import App from './App';
import store from './redux/store';
import { Provider } from 'react-redux';

// Use createRoot from "react-dom/client" instead of ReactDOM.createRoot
const root = createRoot(document.getElementById('root'));

// Render your App component inside BrowserRouter and Provider
root.render(
  <Provider store={store}>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>
);
