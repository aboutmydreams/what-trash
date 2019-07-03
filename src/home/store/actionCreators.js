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
      const data = res.data.content
      const action = getResponseValue(data)
      dispatch(action)
    }).catch( (err) => {
      console.log(err)
    })
  }
}