import React, {useEffect, useState} from 'react';
import {createRoot} from 'react-dom/client';
import {Leaf, Plus, Pencil, Trash2, CheckCircle2, TrendingUp} from 'lucide-react';
import './style.css';

const API='http://localhost:8000/api';
const vazio={nome:'',unidade:'',impacto_estimado:'',progresso:0};

function App(){
 const [itens,setItens]=useState([]),[indic,setIndic]=useState({iniciativas:0,finalizadas:0,progresso_medio:0});
 const [form,setForm]=useState(vazio),[edit,setEdit]=useState(null),[aberto,setAberto]=useState(false);
 async function carregar(){setItens(await (await fetch(`${API}/iniciativas`)).json());setIndic(await (await fetch(`${API}/indicadores`)).json())}
 useEffect(()=>{carregar()},[]);
 async function salvar(e){e.preventDefault();await fetch(`${API}/iniciativas${edit?'/'+edit:''}`,{method:edit?'PUT':'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({...form,progresso:Number(form.progresso)})});setForm(vazio);setEdit(null);setAberto(false);carregar()}
 function editar(i){setForm(i);setEdit(i.id);setAberto(true)}
 async function excluir(id){if(confirm('Excluir esta iniciativa?')){await fetch(`${API}/iniciativas/${id}`,{method:'DELETE'});carregar()}}
 return <div className="app">
  <aside><div className="brand"><span><Leaf/></span><div><b>EcoAção</b><small>Iniciativas Sustentáveis</small></div></div><nav><a className="active">Visão geral</a><a>Iniciativas</a><a>Resultados</a></nav><div className="aside-foot">SEMA/MT<br/><small>Ambiente demonstrativo</small></div></aside>
  <main><header><div><p className="eyebrow">PAINEL DE SUSTENTABILIDADE</p><h1>Iniciativas Sustentáveis</h1><p>Acompanhe ações, impactos e o progresso das unidades.</p></div><button onClick={()=>{setForm(vazio);setEdit(null);setAberto(true)}}><Plus/>Nova iniciativa</button></header>
  <section className="cards"><Card icon={<Leaf/>} label="Iniciativas" value={indic.iniciativas} tone="green"/><Card icon={<CheckCircle2/>} label="Finalizadas" value={indic.finalizadas} tone="blue"/><Card icon={<TrendingUp/>} label="Progresso médio" value={`${indic.progresso_medio}%`} tone="amber"/></section>
  <section className="panel"><div className="panel-head"><div><h2>Portfólio de iniciativas</h2><p>Dados fictícios para demonstração acadêmica</p></div><span>{itens.length} registros</span></div>
  {itens.length?<div className="table"><div className="tr th"><span>Iniciativa</span><span>Unidade</span><span>Impacto estimado</span><span>Progresso</span><span></span></div>{itens.map(i=><div className="tr" key={i.id}><span><b>{i.nome}</b></span><span>{i.unidade}</span><span>{i.impacto_estimado}</span><span><div className="progress"><i style={{width:i.progresso+'%'}}></i></div><small>{i.progresso}%</small></span><span className="actions"><button onClick={()=>editar(i)}><Pencil/></button><button className="danger" onClick={()=>excluir(i.id)}><Trash2/></button></span></div>)}</div>:<div className="empty"><Leaf/><h3>Nenhuma iniciativa cadastrada</h3><p>Cadastre a primeira ação sustentável.</p></div>}
  </section></main>
  {aberto&&<div className="modal"><form onSubmit={salvar}><div className="modal-head"><div><p className="eyebrow">{edit?'EDIÇÃO':'NOVO REGISTRO'}</p><h2>{edit?'Atualizar iniciativa':'Cadastrar iniciativa'}</h2></div><button type="button" className="close" onClick={()=>setAberto(false)}>×</button></div><label>Nome<input required minLength="3" value={form.nome} onChange={e=>setForm({...form,nome:e.target.value})}/></label><label>Unidade<input required value={form.unidade} onChange={e=>setForm({...form,unidade:e.target.value})}/></label><label>Impacto estimado<textarea required value={form.impacto_estimado} onChange={e=>setForm({...form,impacto_estimado:e.target.value})}/></label><label>Progresso: <b>{form.progresso}%</b><input type="range" min="0" max="100" value={form.progresso} onChange={e=>setForm({...form,progresso:e.target.value})}/></label><div className="form-actions"><button type="button" className="secondary" onClick={()=>setAberto(false)}>Cancelar</button><button type="submit">Salvar iniciativa</button></div></form></div>}
 </div>
}
function Card({icon,label,value,tone}){return <div className={'card '+tone}><span className="icon">{icon}</span><div><p>{label}</p><strong>{value}</strong></div></div>}
createRoot(document.getElementById('root')).render(<App/>);
