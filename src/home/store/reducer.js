const defaultValue = {
  inputValue: '陶瓷是什么垃圾？',
  list: [],
  resList: []
}

export default (state = defaultValue, action) => {
  if (action.type === 'change_input_value') {
    const newState = JSON.parse(JSON.stringify(state))
    newState.inputValue = action.value
    return newState
  }
  if (action.type === 'add_item') {
    const newState = JSON.parse(JSON.stringify(state))
    newState.list.push(newState.inputValue)
    newState.inputValue = ''
    return newState
  }
  if (action.type === 'get_response_value') {
    const newState = JSON.parse(JSON.stringify(state))
    console.log("action.data", action.data)
    newState.resList.push(action.data)
    return newState
  }
  return state
}