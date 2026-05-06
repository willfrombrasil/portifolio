import re
import json

def expand_phases(name, base_phases):
    phases = []
    for i in range(1, 11):
        phase = {
            "num": i,
            "title": f"Fase {i} - Aprofundamento em {name}",
            "topics": [f"Conceito {name} - Nível {i}.{j}" for j in range(1, 11)],
            "practice": [f"Exercício prático {name} - Atividade {j}" for j in range(1, 6)],
            "project": [f"Projeto principal {j} - Fase {i}" for j in range(1, 4)],
            "challenge": [f"Desafio mestre {name} - Extra {j}" for j in range(1, 4)]
        }
        phases.append(phase)
    return phases

docs_html = [
    {"name": "MDN Web Docs", "url": "https://developer.mozilla.org/pt-BR/docs/Web/HTML"},
    {"name": "WHATWG", "url": "https://html.spec.whatwg.org/"},
    {"name": "W3C HTML5", "url": "https://www.w3.org/TR/html52/"},
    {"name": "W3Schools HTML", "url": "https://www.w3schools.com/html/"}
]

docs_css = [
    {"name": "MDN Web Docs", "url": "https://developer.mozilla.org/pt-BR/docs/Web/CSS"},
    {"name": "W3C CSS", "url": "https://www.w3.org/Style/CSS/"},
    {"name": "CSS-Tricks", "url": "https://css-tricks.com/"},
    {"name": "Smashing Magazine", "url": "https://www.smashingmagazine.com/category/css/"},
    {"name": "BEM", "url": "https://getbem.com/"},
    {"name": "Bootstrap", "url": "https://getbootstrap.com/docs/"},
    {"name": "Tailwind CSS", "url": "https://tailwindcss.com/docs"}
]

docs_js = [
    {"name": "MDN Web Docs", "url": "https://developer.mozilla.org/pt-BR/docs/Web/JavaScript"},
    {"name": "ECMA International", "url": "https://tc39.es/ecma262/"},
    {"name": "JavaScript.info", "url": "https://javascript.info/"},
    {"name": "freeCodeCamp", "url": "https://www.freecodecamp.org/learn/"},
    {"name": "Node.js", "url": "https://nodejs.org/en/docs"},
    {"name": "npm", "url": "https://docs.npmjs.com/"},
    {"name": "Fetch API", "url": "https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API"},
    {"name": "Jest", "url": "https://jestjs.io/docs/getting-started"}
]

docs_php = [
    {"name": "Design Patterns", "url": "https://refactoring.guru/design-patterns"},
    {"name": "PHP The Right Way", "url": "https://phptherightway.com/"},
    {"name": "PHP-FIG (PSR)", "url": "https://www.php-fig.org/psr/"},
    {"name": "Composer", "url": "https://getcomposer.org/doc/"},
    {"name": "PHP.net Docs", "url": "https://www.php.net/docs.php"},
    {"name": "PHP.net Manual", "url": "https://www.php.net/manual/pt_BR/"},
    {"name": "PHPUnit", "url": "https://phpunit.de/documentation.html"},
    {"name": "Pest", "url": "https://pestphp.com/docs"},
    {"name": "PHP Sandbox", "url": "https://onlinephp.io/"},
    {"name": "REST Test", "url": "https://resttesttest.com/"}
]

docs_mysql = [
    {"name": "MySQL", "url": "https://dev.mysql.com/doc/"},
    {"name": "W3Schools MySQL", "url": "https://www.w3schools.com/mysql/"},
    {"name": "MySQL Tutorial", "url": "https://www.mysqltutorial.org/"},
    {"name": "phpMyAdmin", "url": "https://docs.phpmyadmin.net/"},
    {"name": "MariaDB", "url": "https://mariadb.com/kb/en/documentation/"},
    {"name": "PostgreSQL", "url": "https://www.postgresql.org/docs/"},
    {"name": "Eloquent ORM", "url": "https://laravel.com/docs/eloquent"},
    {"name": "Doctrine", "url": "https://www.doctrine-project.org/projects/doctrine-orm/en/current/"}
]

docs_infra = [
    {"name": "GitHub", "url": "https://docs.github.com/"},
    {"name": "Docker", "url": "https://docs.docker.com/"},
    {"name": "Laradock", "url": "https://laradock.io/"},
    {"name": "Laragon", "url": "https://laragon.org/"},
    {"name": "VS Code", "url": "https://code.visualstudio.com/docs"},
    {"name": "Sublime Text", "url": "https://www.sublimetext.com/docs/"},
    {"name": "Vercel", "url": "https://vercel.com/docs"},
    {"name": "Supabase", "url": "https://supabase.com/docs"}
]

roadmapData = {
    "html": {
        "title": "Roadmap — HTML (Estrutura e Semântica)",
        "desc": "A base estrutural de toda a web.",
        "icon": "fa-brands fa-html5 text-orange-500",
        "docs": docs_html,
        "phases": expand_phases("HTML", [])
    },
    "css": {
        "title": "Roadmap — CSS (Estilização e Layout)",
        "desc": "Dando vida e beleza às páginas web.",
        "icon": "fa-brands fa-css3-alt text-blue-500",
        "docs": docs_css,
        "phases": expand_phases("CSS", [])
    },
    "js": {
        "title": "Roadmap — JavaScript (Lógica)",
        "desc": "Interatividade e comportamento dinâmico. O motor do Frontend.",
        "icon": "fa-brands fa-square-js text-yellow-400",
        "docs": docs_js,
        "phases": expand_phases("JavaScript", [])
    },
    "php": {
        "title": "Roadmap — PHP 8 (Backend e Arquitetura)",
        "desc": "O cérebro por trás de aplicações web robustas e seguras.",
        "icon": "fa-brands fa-php text-indigo-500",
        "docs": docs_php,
        "phases": expand_phases("PHP 8", [])
    },
    "mysql": {
        "title": "Roadmap — Bancos de Dados & ORM",
        "desc": "Armazenamento e modelagem de dados de alta performance.",
        "icon": "fa-solid fa-database text-blue-400",
        "docs": docs_mysql,
        "phases": expand_phases("Bancos de Dados", [])
    },
    "infra": {
        "title": "Roadmap — Infraestrutura & Ferramentas",
        "desc": "DevOps, IA, Containers e Produtividade.",
        "icon": "fa-solid fa-server text-gray-500",
        "docs": docs_infra,
        "phases": expand_phases("Infra e Ferramentas", [])
    },
    "cursos": {
        "title": "Cursos e Treinamentos Recomendados",
        "desc": "Links diretos para acelerar sua jornada de arquiteto de software.",
        "icon": "fa-solid fa-graduation-cap text-green-500",
        "isLinkList": True,
        "items": [
            { "name": "Fundamentos PHP 7/8 - EspecializaTi", "url": "https://academy.especializati.com.br/curso/fundamentos-programacao-php-7", "tag": "Backend" }
        ]
    }
}

import codecs
html = codecs.open("roadmap.html", "r", "utf-8").read()
# match const roadmapData = { ... }; let currentSection = 'html';
pattern = re.compile(r"const roadmapData = \{.*?\};[\r\n\s]*let currentSection = 'html';", re.DOTALL)
json_str = json.dumps(roadmapData, indent=4, ensure_ascii=False)
new_js = f"const roadmapData = {json_str};\n        let currentSection = 'html';"
html = pattern.sub(new_js, html)

# Agora trocar a renderização para projetos iteráveis e add links
render_pattern = re.compile(r"card\.innerHTML = `(.*?)`;\s+container\.appendChild\(card\);", re.DOTALL)

new_render = """
let projectHtml = Array.isArray(phase.project) ? phase.project.map(p => `<li><i class="fa-solid fa-rocket mr-2 text-primary"></i>${p}</li>`).join('') : `<i class="fa-solid fa-rocket mr-2"></i>${phase.project}`;

card.innerHTML = `
    <div class="p-6 border-b border-gray-100 dark:border-gray-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="flex items-center gap-4">
            <div class="flex-shrink-0 w-12 h-12 bg-gray-100 dark:bg-gray-800 rounded-full flex items-center justify-center border-2 border-primary/20">
                <span class="text-xl font-bold text-primary">${phase.num}</span>
            </div>
            <div>
                <h3 class="text-lg font-bold text-gray-900 dark:text-white">Fase ${phase.num}: ${phase.title}</h3>
            </div>
        </div>
    </div>
    
    <div class="p-6 grid grid-cols-1 md:grid-cols-2 gap-6">
        <div>
            <h4 class="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-3 flex items-center gap-2">
                <i class="fa-solid fa-book text-blue-500"></i> Conceitos Chave
            </h4>
            <ul class="space-y-2 h-64 overflow-y-auto pr-2 custom-scrollbar">
                ${phase.topics.map(t => `<li class="flex items-start gap-2 text-sm text-gray-700 dark:text-gray-300"><i class="fa-solid fa-check text-green-500 mt-1 flex-shrink-0"></i> <span>${t}</span></li>`).join('')}
            </ul>
        </div>
        
        <div>
            <h4 class="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-3 flex items-center gap-2">
                <i class="fa-solid fa-keyboard text-purple-500"></i> Exercícios Práticos
            </h4>
            <ul class="space-y-2">
                ${phase.practice.map(p => `<li class="flex items-start gap-2 text-sm text-gray-700 dark:text-gray-300"><i class="fa-solid fa-code text-gray-400 mt-1 flex-shrink-0"></i> <span>${p}</span></li>`).join('')}
            </ul>
        </div>
    </div>

    <div class="bg-gray-50 dark:bg-gray-800/50 p-6 flex flex-col md:flex-row gap-4 justify-between items-start border-t border-gray-100 dark:border-gray-800">
        <div class="flex-1 w-full">
            <span class="text-xs font-semibold text-gray-500 uppercase">Projetos Finais da Fase</span>
            <ul class="font-bold text-lg mt-1 space-y-1">
                ${projectHtml}
            </ul>
        </div>
        <div class="flex-1 w-full md:text-right">
            <span class="text-xs font-semibold text-gray-500 uppercase">Desafios Extras</span>
            <div class="mt-2 flex flex-wrap gap-2 md:justify-end">
                ${phase.challenge.map(c => `<span class="px-2 py-1 bg-red-100 text-red-700 dark:bg-red-900/30 dark:text-red-400 rounded text-xs font-medium"><i class="fa-solid fa-fire mr-1"></i>${c}</span>`).join('')}
            </div>
        </div>
    </div>
`;
container.appendChild(card);
"""
html = render_pattern.sub(new_render.strip(), html)

# add docs header
doc_inject = """document.getElementById('trailDesc').textContent = data.desc;
            
            const container = document.getElementById('phasesContainer');
            container.innerHTML = '';

            // Render Docs Se existir
            if(data.docs) {
                const docsHtml = `<div class="mb-6 p-4 rounded-xl bg-gray-100 dark:bg-gray-800 border border-gray-200 dark:border-gray-700">
                    <h3 class="text-sm font-bold text-gray-800 dark:text-gray-200 mb-3"><i class="fa-solid fa-link mr-2 text-blue-500"></i>Documentação Externa Recomendada</h3>
                    <div class="flex flex-wrap gap-3">
                        ${data.docs.map(d => `<a href="${d.url}" target="_blank" class="text-xs inline-flex items-center gap-1 bg-white dark:bg-darkBg px-3 py-1.5 rounded-full border border-gray-300 dark:border-gray-600 hover:text-primary transition"><i class="fa-brands fa-chrome text-gray-400"></i> ${d.name}</a>`).join('')}
                    </div>
                </div>`;
                container.innerHTML += docsHtml;
            }"""

html = html.replace("document.getElementById('trailDesc').textContent = data.desc;\n            \n            const container = document.getElementById('phasesContainer');\n            container.innerHTML = '';", doc_inject)


codecs.open("roadmap.html", "w", "utf-8").write(html)
print("Updated successfully")
