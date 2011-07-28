\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{cefet}[2011/07/27 Classe modelo para monografias de TCC do CEFET-MG Campus Leopoldina]

\RequirePackage{ifthen}
\RequirePackage{calc}
\RequirePackage{graphicx}
\RequirePackage[T1]{fontenc}
\RequirePackage[utf8]{inputenc}
\RequirePackage{times}

\LoadClassWithOptions{abnt}

\setlength{\parindent}{1.5cm}

\renewcommand{\rmdefault}{ugm}

\renewcommand{\capa}{
    \@restonecolfalse\newpage
    \thispagestyle{empty}
    \begin{center}
        \begin{espacosimples}
            \setlength{\parskip}{0.3cm}
            \includegraphics[width=1.26in]{imagens/cefet.eps}\par
            CENTRO FEDERAL DE EDUCAÇÃO TECNOLÓGICA DE MINAS GERAIS\par
            \textit{Campus} III - Leopoldina\par
            Engenharia de Controle e Automação
        \end{espacosimples}
    \end{center}
    \vspace*{1cm}
    \vfill\vfill
    \ABNTifnotempty{\ABNTtitulodata}{
        \begin{center}
            \begin{espacosimples}
                \LARGE\bf\ABNTtitulodata
            \end{espacosimples}
        \end{center}
    }
    \vfill\vfill
    \ABNTifnotempty{\ABNTautordata}{
        \begin{center}
            \Large\em\ABNTautordata
        \end{center}
    }
    \vspace*{1.5cm}
    \vfill\vfill
    \begin{center}
        \begin{espacosimples}
            \setlength{\parskip}{.3cm}
            \ABNTifnotempty{\ABNTlocaldata}
                {{\localformat\ABNTlocaldata}\par}
            \ABNTifnotempty{\ABNTdatadata}
                {{\dataformat\ABNTdatadata}}
        \end{espacosimples}
    \end{center}
    \vspace*{1cm}
    \newpage
    \espaco{\ABNTespacodefault}
}

\renewenvironment{folhadeaprovacao}{
    \clearpage{}
    \thispagestyle{empty}
    \begingroup
    \setlength{\parindent}{0cm}
    \begin{center}
        \setlength{\parskip}{.3cm}
        \bf\ABNTtitulodata\par
        \large\textit{\ABNTautordata}
    \end{center}
    \vspace*{1cm}
    Trabalho de Conclusão de Curso submetido à Banca examinadora instituída pelo
    \ABNTinstituicaodata, como parte dos requisitos necessários para a obtenção
    do grau de Engenheiro de Controle e Automação.
    \vspace*{.3cm}
    \begin{center}
        Banca Examinadora:
    \end{center}
    \setlength{\ABNTsignthickness}{0.5pt}
    \setlength{\ABNTsignskip}{2.2cm}
    \setlength{\ABNTsignwidth}{10cm}
    \begin{flushright}
}{
    \end{flushright}
    \vfill\vfill
    \begin{center}
        \begin{espacosimples}
            \setlength{\parskip}{.3cm}
            \ABNTifnotempty{\ABNTlocaldata}
                {{\localformat\ABNTlocaldata}\par}
            \ABNTifnotempty{\ABNTdatadata}
                {{\dataformat\ABNTdatadata}}
        \end{espacosimples}
    \end{center}
    \newpage
    \espaco{\ABNTespacodefault}
    \endgroup{}
    \clearpage{}
}

\renewenvironment{resumo}{
    \clearpage
    \setchaptertype{resumo}
    \setlength{\parindent}{0cm}
    \setlength{\parskip}{0.7cm}
    \begin{center}
        \textbf{\ABNTtitulodata} \\
        \ABNTautordata \\
        \ABNTdatadata
    \end{center}\par{}
    \textbf{Orientador:} \ABNTorientadordata{}
    \vspace*{2.5cm}
}{}

\renewenvironment{abstract}{
    \clearpage
    \setchaptertype{abstract}
    \setlength{\parindent}{0cm}
    \setlength{\parskip}{0.7cm}
}{}

\newenvironment{agradecimentos}{
    \clearpage
}{}

\setlength{\parskip}{.4cm}
