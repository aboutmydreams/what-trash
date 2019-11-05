import React from 'react';
import { connect } from 'react-redux';
import { addInputItem, changeInputValue, toGetResponse } from './store/actionCreators';
import _ from 'lodash'

const Home = (props) => {
  return (
      <div style={styles.container}>
        <div style={styles.header}>
          what-trash
        </div>
        <div id="cont" style={styles.content}>
          <div style={styles.content.response}>
            <img style={styles.avator} alt='浩浩机器人的头像' src="http://img.flura.cn/robot.jpg"></img>
            <div style={styles.content.msg}>
              <span style={styles.content.response.info}>我是小小垃圾分类助手，告诉我你想进行分类的任何垃圾哟~</span>
            </div>           
          </div>
          {
            props.list.map((item, index) => {
              return ( 
              <div key={index}>
                <div style={styles.content.item}>
                  <div style={styles.content.msg}>
                    <span style={styles.content.item.info}>{item}</span>
                  </div>
                  <img style={styles.avator} alt='你的头像' src={`https://exqlnet-note.oss-cn-shenzhen.aliyuncs.com/star/${RandomNum}.png`}></img>
                </div>
                <div style={styles.content.response} >
                <img style={styles.avator} alt='浩浩机器人的头像' src="http://img.flura.cn/robot.jpg"></img>
                  <div style={styles.content.msg}>
                    <span style={styles.content.response.info}>{props.response[index]}</span>
                  </div>           
                </div>
              </div>
              )
            }) 
          }
        </div>
        <form style={styles.footer} onSubmit={e => {props.handleSubmit(e, props)} }>
          <input type="text"  style={styles.footer.input} value={props.inputValue}  onChange={ props.handleInputValue }></input>
          <button style={styles.footer.button}>发送</button>
        </form>
      </div>
  )
  
}

const RandomNum = _.random(1,3) //随机数，为了从cdn里随机挑选一个头像

const styles = {
  container : {
    margin: '0 auto',
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'flex-end',
    color: 'white',
  },
  header: {
    position: 'fixed',
    top: '0',
    width: '100%',
    height: '50px',
    lineHeight: '50px',
    textAlign: 'center',
    background: '#01AFFF',
  },
  avator: {
    width: '45px',
    height: '45px',
    margin: '0 10px',
    border: '0',
    borderRadius: '50%',
  },
  content: {
    position: 'fixed',
    top: '50px',
    bottom: '55px',
    overflowY: 'scroll',
    flex: 1,
    width: '100%',
    background: '#F1F2F7',
    msg: {
      width: '70%',
      position: 'relative',
    },

    item: {
      display: 'flex',
      justifyContent: 'flex-end',
      textAlign: 'right',
      info: {
        display: 'inline-block',
        padding: '10px 15px',
        backgroundColor: '#1FBAFC',
        boxShadow: '0px 0px 2px #1FBAFD',
        borderRadius: '15px',
      },
    },

    response: {
      display: 'flex',
      justifyContent: 'flex-start',
      textAlign: 'left',
      margin: '10px 0',
      info: {
        display: 'inline-block',
        padding: '10px 10px',
        background: '#ffffff',
        borderRadius: '15px',
        color: 'black',
        wordWrap: 'break-word',
      }
    }

  },
  footer: {
    position: 'fixed',
    bottom: '0', 
    // maxWidth: '420px',
    paddingTop: '8px',
    width: '100%',
    display: 'flex',
    background: '#ececf4',
    height: '50px',
    lineHeight: '50px',
    input: {
      flex: '1',
      marginLeft: '10px',
      paddingLeft: '15px',
      height: '40px',
      lineHeight: '40px',
      fontSize: '16px',
      border: 'none',
      borderRadius: '20px',
      outline: 'none',
    },
    button: {
      width: '70px',
      height: '40px',
      marginLeft: '10px',
      marginRight: '10px',
      borderRadius: '20px',
      border: 'none',
      background: '#1FBAFC',
      color: '#ffffff'
    }
  },
  
}

const mapStateToProps = (state) => {
  return {
    inputValue: state.inputValue,
    list: state.list,
    response: state.resList,
  }
}

const mapDispatchToProps = (dispatch) => {
  return {
    handleInputValue(e) {
      const action = changeInputValue(e.target.value)
      dispatch(action)
    },
    handleSubmit(e, props) {
      e.preventDefault()
      if (props.inputValue !== '') {
        const action = addInputItem()
        dispatch(action)
        const param = {"name": props.inputValue}
        // console.log("param", param)
        const resAction = toGetResponse(param)
        dispatch(resAction)
        setTimeout(() => {
          this.scrollButtom()
        }, 0);
      } else {
        console.log("input不能为空")
      }
    },
    scrollButtom() {
      let cont = document.getElementById("cont")
      cont.scrollTop = cont.scrollHeight
    }

  }
}


export default connect(mapStateToProps, mapDispatchToProps)(Home);
