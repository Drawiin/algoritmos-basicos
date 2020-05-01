const request = require('request')
const dotenv = require('dotenv')
const fs = require('fs')

dotenv.config()

async function sendAnswer() {
  try {
    const options = {
      url: `https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=${process.env.TOKEN}`,
      headers: {
        "Content-Type": "multipart/form-data"
      },
      formData: {
        "answer": fs.createReadStream("./answer.json")
      }
    }

    request.post(options, function (err, res, body) {
      if (err) console.log(err);
      console.log(body);
    })

  } catch (error) {
    console.log(error)
  }
}

sendAnswer()