require('dotenv').config({ silent: true })
const express = require('express')
const cors = require('cors')
const middleWarez = require('./index.js')
const port = process.env.PORT || 3000

const app = express()

// --- CONFIGURAÇÃO DO CORS ---
// Defina os domínios permitidos (whitelist)
const whitelist = [
  'https://czargab18.github.io'
]

const corsOptions = {
  origin: function (origin, callback) {
    // Permite requisições sem 'origin' (como Postman, curl, etc.)
    // e requisições de domínios na whitelist
    if (!origin || whitelist.indexOf(origin) !== -1) {
      callback(null, true)
    } else {
      callback(new Error('Acesso negado pelo CORS - Domínio não autorizado'))
    }
  },
  credentials: true // Permite envio de cookies/credenciais
}

// Aplica o middleware CORS em todas as rotas
app.use(cors(corsOptions))
// --- FIM DA CONFIGURAÇÃO DO CORS ---

// Initial page redirecting to Github
app.get('/auth', middleWarez.auth)

// Callback service parsing the authorization token
// and asking for the access token
app.get('/callback', middleWarez.callback)

app.get('/success', middleWarez.success)

// REMOVIDO: app.get('/', middleWarez.index)
// A rota raiz (/) agora retornará 404 - API não precisa de página index

app.listen(port, () => {
  console.log("Netlify CMS OAuth provider listening on port " + port)
  console.log("CORS habilitado para:", whitelist.join(', '))
})
