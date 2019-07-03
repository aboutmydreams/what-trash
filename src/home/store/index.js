import { createStore, applyMiddleware, compose} from 'redux';
import reducer from './reducer'  //reducer 
import thunk from 'redux-thunk'

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ ?   
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__({ }) : compose;

const enhancer = composeEnhancers(
  applyMiddleware(thunk),
  // other store enhancers if any
);

const store = createStore(
  reducer,
  enhancer
);  //将reducer传入 创建store  store可以去reducer中查看数据了

export default store;