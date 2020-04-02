const sha1 = require('sha1')
const fs = require('fs')

try {
  const jsonString = fs.readFileSync('./answer.json')
  const answer = JSON.parse(jsonString)
  const decodedMessage = cesarShiftDecoder(answer.cifrado, answer.numero_casas)
  const hash = sha1(decodedMessage)

  answer.decifrado = decodedMessage
  answer.resumo_criptografico = hash
  
  fs.writeFileSync('./answer.json', JSON.stringify(answer, null, 2))
} catch(err) {
  console.log(err)
  return
}


function cesarShiftDecoder(message, shift){
  const unshift = 26 - shift
  return String.fromCharCode(
    ...message.toLowerCase()
      .split('')
        .map(char => {
          return char.match(/[a-z]/i)
            ? ((char.charCodeAt(0) - 97 + unshift) % 26) + 97 
            : char.charCodeAt(0)
        })
  )
}
