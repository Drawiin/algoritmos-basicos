const axios = require('axios').default
const dotenv = require('dotenv')
const fs = require('fs')

dotenv.config()

async function loadAndStore(){
  try {
    const response = await axios.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data',{
      params:{
        token: process.env.TOKEN
      }
    })
    fs.writeFileSync('./answer.json', JSON.stringify(response.data, null, 2))
  } catch (error) {
    console.log(error)
  }
}

loadAndStore()