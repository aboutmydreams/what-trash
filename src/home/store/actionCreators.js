import { ADD_ITEM, CHANGE_INPUT_VALUE,  GET_RESPONSE_VALUE} from './actionType'
import axios from 'axios'

export const addInputItem = (value) => ({
  type: ADD_ITEM,
  value
})

export const changeInputValue = (value) => ({
  type: CHANGE_INPUT_VALUE,
  value
})

export const getResponseValue = (data) => ({
  type: GET_RESPONSE_VALUE,
  data
})

export const toGetResponse = (param) => {
  return (dispatch) => {
    axios.get('http://118.25.236.82:1028/trash',{params: param}).then((res) =>{
        if (res) {
          const data = res.data.content
          const action = getResponseValue(data)
          dispatch(action)
        } else {
          const data = '我有点反应不过来'
          const action = getResponseValue(data)
          dispatch(action)
        }
       
    }).catch( (err) => {
        const data = '我有点不太明白你在说什么'
        const action = getResponseValue(data)
        dispatch(action)
      console.log(err)
    })
  }
}