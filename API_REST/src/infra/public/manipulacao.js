
function enviarDados(){
    const usuario = document.getElementById('login')
    const senha = document.getElementById('senha')
    const dados = document.getElementById('form-usuario')

    
    dados.onsubmit = async (event) =>{
        event.preventDefault()
        const nome_usuario = usuario.value
        const senha_usuario = senha.value
    
        await axios.post('http://127.0.0.1:8000/usuarios', {
            nome: nome_usuario,
            senha: senha_usuario
        })
    console.log('Cadastrado com sucesso')    
    alert('Cadastro realizado com sucesso!')

}
}

function app(){
    console.log("App Iniciada")
    enviarDados()
}
app()
