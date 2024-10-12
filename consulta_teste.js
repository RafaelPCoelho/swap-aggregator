const { ethers } = require("ethers");
const SushiSwapABI = require("./sushiSwapABI.json");
require('dotenv').config();

// Endereço do contrato Router da SushiSwap na Ethereum Mainnet
const SUSHISWAP_ROUTER_ADDRESS = ethers.getAddress("0xd9e1cE17f2641f24aE83637ab66a2cca9C378B9F"); 

// Endereços dos tokens (exemplo: USDT e DAI na Ethereum Mainnet)
const USDT_ADDRESS = "0xdAC17F958D2ee523a2206206994597C13D831ec7";
const DAI_ADDRESS = "0x6B175474E89094C44Da98b954EedeAC495271d0F";

// ABI mínima do contrato Router da SushiSwap
const SUSHISWAP_ROUTER_ABI = SushiSwapABI;

// Função principal para fazer a consulta
async function consultaSwap() {
    // Configurando o provider (aqui usando o provedor padrão da ethers)
    const provider = new ethers.AlchemyProvider('mainnet',process.env.ALCHEMY_KEY);

    // Verificar se o provider foi configurado corretamente
    console.log("Provider configurado:");

    // Instanciando o contrato do Router da SushiSwap
    const routerContract = new ethers.Contract(SUSHISWAP_ROUTER_ADDRESS, SUSHISWAP_ROUTER_ABI, provider);

    // Quantidade de USDT que você quer trocar (exemplo: 100 USDT, valor em wei)
    const amountIn = ethers.parseEther("100", 6); // 6 decimais para USDT

    // Caminho da troca: USDT -> DAI
    const path = [USDT_ADDRESS, DAI_ADDRESS];

    // Exibir valores antes da consulta
    console.log("Consultando troca de", ethers.formatUnits(amountIn, 6), "USDT para DAI");
    console.log("Caminho de troca:", path);

    // Fazendo a consulta na pool
    try {
        const amountsOut = await routerContract.getAmountsOut(amountIn, path);
        console.log("Resultado bruto da consulta (em wei):", amountsOut);

        const amountOut = ethers.formatUnits(amountsOut[1], 18); // DAI tem 18 decimais
        console.log(`Para trocar 100 USDT, você receberá aproximadamente ${amountOut} DAI.`);
    } catch (error) {
        console.error("Erro ao consultar a pool:", error);
    }
}

// Chamando a função
consultaSwap();
