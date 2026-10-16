-- Apupiwe: abstract syntax (the meanings the language can express).
-- Each function names the reference rule(s) it implements (docs/language.md, anchors #r-4-2-4 = 4.2.4).
-- Content words come from the generated Lex (one function per role: thing N, event V, quality A).
-- Grammar-word and digit functions keep their v1 names (Tan is THIS, now win; Fi is the digit 1, now ni;
-- MinP is the question particle, now bi; Mu is NOT, now su ...); ApupiweApu has the current forms
-- (short-word layer, design log 2026-10-15).
abstract Apupiwe = Lex ** {
  flags startcat = Utt ;

  cat
    Utt ;      -- a whole sentence: slots 1-13 (4.1.2)
    Sent ;     -- slots 2-11: openers, then the core (4.1.2, 4.3.4)
    Core ;     -- slots 3-11: speech act, then a clause or fragment
    Call ;     -- a person word calling someone (10.1.1)
    CallOpt ; LinkOpt ; FrameOpt ; CondOpt ; Tail ;
    Linker ;   -- bo win, ka, yen (4.3.6)
    Act ;      -- speech-act particle with politeness (7.1, 10.2)
    Part ;     -- one speech-act particle (7.1.1)
    PMod ;     -- genso / ba before a particle (7.1.3)
    Nun ;      -- politeness (10.2.1)
    Stance ;   -- stance word (7.2)
    Cl ;       -- a clause with its clause operators (slots 5-11)
    Cl0 ;      -- subject and predicate (slots 6-11)
    ConfOpt ; SrcOpt ;
    VP ;       -- predicate, possibly verbs joined by yen/lu/ka (4.4.7)
    VPo ;      -- one predicate with its phrase operators, habit and aspect (slot 7, 6.2.7)
    VPa ;      -- verb, objects, relation phrases, trailing clause (slots 8-11)
    VPm ;      -- verb and objects, or a verb with no object and a bare word saying how (slots 8-9)
    VPc ;      -- verb and objects (slots 8-9)
    VPs ;      -- a predicate missing its object, inside a relative clause (5.3.3)
    HabOpt ; AspOpt ; Asp ; Op ;
    Manner ;   -- a bare word saying how, after a verb with no object (4.2.4, 4.2.6)
    AP ;       -- a quality phrase
    Adv ;      -- relation phrase or linked clause (4.4)
    Prep ;     -- relation word (4.4.1, 13.2)
    Sub ;      -- don, bo: linkers taking a clause (4.3.3)
    NP ;       -- noun phrase, possibly a yen/lu list (4.4.5)
    NPi ;      -- one noun phrase: a list item and a pi complement (5.2.9)
    NPq ;      -- noun, modifiers, number, la, determiner, label (5.1.1)
    CN ;       -- noun and content modifiers (5.2.1)
    Rel ;      -- relative clause (5.3)
    NumOpt ; LaOpt ; DetOpt ;
    Pron ; Det ; Deriv ; Conj ;
    Digit ; Sub100 ; Sub1000 ; Num ; Digs ;

  fun
    -- 4.1 The sentence template --------------------------------------------------------
    MkUtt : CallOpt -> Sent -> Tail -> CallOpt -> Utt ;   -- 4.1.2 slots 1, 12, 13; 10.1.1
    NoCall : CallOpt ;                     -- 4.1.1 only the verb is required
    SomeCall : Call -> CallOpt ;           -- 10.1.1, 4.6.2: "X , ..." at the start or ", X" at the end
    CallName : String -> Call ;            -- 10.1.1 fo + name
    CallNameFi : String -> Call ;          -- 5.2.12, 10.1.1 fo + name + fi
    CallN : N -> Call ;                    -- 4.1.2 slot 1: a single role or kin word
    CallLanno : Call ;                     -- 10.1.3 lanno alone in address
    LannoCall : Call -> Call ;             -- 10.1.3 lanno before a name, role or kin word
    NoTail : Tail ;                        -- 4.1.1
    StanceTail : Stance -> Tail ;          -- 7.2.1, 4.6.7: ", bi" / ", yan" ...
    StanceMin : Stance -> Tail ;           -- 7.2.7: two stance words, one pause before both, bi last
    ChoiceYu : Tail ;                      -- 4.8.4, 4.6.7: ", yu" which?
    MinSt, ASt, Buni, Donon : Stance ;     -- 7.2.2-7.2.5

    MkSent : LinkOpt -> FrameOpt -> CondOpt -> Core -> Sent ;  -- 4.3.4 linker, scene/topic, if/when
    NoLink : LinkOpt ;                     -- 4.1.1
    Link : Linker -> LinkOpt ;             -- 4.3.6, 4.6.3
    GiTan, UnL, YenL : Linker ;            -- 4.3.6; 6.2.4 yen "also, ..."
    NoFrame : FrameOpt ;                   -- 4.1.1
    Scene : Adv -> FrameOpt ;              -- 4.3.1 a relation phrase sets the scene
    Topic : NP -> FrameOpt ;               -- 4.3.2 pi + noun phrase, to its pause or kiyo
    NoCond : CondOpt ;                     -- 4.1.1
    Cond : Adv -> CondOpt ;                -- 4.3.3 don/lin/kon/ya/bo + clause

    -- speech acts (7.1) and politeness (10.2)
    Stmt : Cl -> Core ;                    -- 4.2.8, 7.1.2 no particle: a statement
    ActCl : Act -> Cl -> Core ;            -- 4.1.2 slot 3
    FragNP : NP -> Core ;                  -- 4.5.1 just the new part
    FragAdv : Adv -> Core ;                -- 4.5.1
    FragAP : AP -> Core ;                  -- 4.5.2 a bare state: ten upe
    PartAct : Part -> Act ;                -- 7.1.2 one speech act
    PartNun : Part -> Nun -> Act ;         -- 10.2.1 fin right after the particle
    NunAct : Nun -> Act ;                  -- 10.2.1 fin where the particle would be
    Nun1, NunNun : Nun ;                   -- 10.2.1, 1.5
    MinP, So, Tin, Fon, De, Yo, BaP, GensoP : Part ;   -- 7.1.1
    YoYo, GensoGenso : Part ;              -- 7.1.1, 1.5 doubling
    ModPart : PMod -> Part -> Part ;       -- 7.1.3 genso bi, ba bi
    GensoM, BaM : PMod ;                   -- 7.1.3

    -- 6.1 clause operators
    MkCl : ConfOpt -> SrcOpt -> Cl0 -> Cl ;  -- 4.1.2 slot 5
    NoConf : ConfOpt ;                     -- 1.1, 6.1.2 an unmarked statement is believed
    Kon : Num -> ConfOpt ;                 -- 6.1.2 pe + sixths
    KonOf : Num -> Num -> ConfOpt ;        -- 6.1.2 pe + exact chance, n pi m (out of 100)
    KonBo : ConfOpt ;                      -- 6.1.2 pe pa "maybe"
    NoSrc : SrcOpt ;                       -- 1.1, 6.1.3 source is optional
    Wanme, Inwun, Wemen : SrcOpt ;         -- 6.1.3

    -- clauses
    PredCl : NP -> VP -> Cl0 ;             -- 1.2 subject, verb, object; 4.6.4 pause after an open subject
    NoSubj : VP -> Cl0 ;                   -- 4.5.1, 4.5.2, 4.7.6, 4.7.7 subject left out
    ConjCl : Cl -> Conj -> Cl -> Cl ;      -- 4.4.5, 4.6.6 clauses joined; the second has a subject

    -- slot 7: operators, habit, aspect (6.2, 8.1)
    UseVPo : VPo -> VP ;                   -- 4.1.2 slot 8: one verb
    ConjVP : VPo -> Conj -> VP -> VP ;     -- 4.4.7 separate predicates; 4.4.4 later material to the last; 4.6.6
    PredVP : HabOpt -> AspOpt -> VPa -> VPo ;  -- 6.2.7 manni, then aspect, then the verb
    OpVP : Op -> VPo -> VPo ;              -- 6.2.1 an operator before the verb covers the predicate
    StillNot : HabOpt -> VPa -> VPo ;      -- 8.1.3, 6.2.7 le su "still not, not yet": aspect before su
    NoHab : HabOpt ;                       -- 1.1
    Manni : HabOpt ;                       -- 8.1.4
    NoAsp : AspOpt ;                       -- 8.1.1 tense is optional; 1.1
    SomeAsp : Asp -> AspOpt ;              -- 8.1.2 aspect words come right before the verb
    Sin, Le, Buntu : Asp ;                 -- 8.1.2
    SinLe : Asp ;                          -- 8.1.2 sin le "was doing, had been doing"
    Mu, Na, Fe, Wi, O, Konsin, Nedin : Op ;   -- 6.2.2-6.2.5
    Ke, Bi, Tason : Op ;                   -- 6.2.6 degree
    MuMu : Op ;                            -- 1.5 emphatic not

    -- slots 10-11: relation phrases (manner is fun + a word, 4.2.4), trailing clauses (4.4)
    UseVPm : VPm -> VPa ;                  -- 4.1.2 slots 10-11 empty
    AdvVP : VPa -> Adv -> VPa ;            -- 4.4.1 attaches to the clause's verb; 4.4.4 innermost; 4.6.9;
                                           -- 4.2.6 after an object verb, to that verb
    UseVPc : VPc -> VPm ;                  -- 4.1.2
    MannerVP : VPc -> Manner -> VPm ;      -- 4.2.4 a verb with no object, then a bare word saying how
    BareManner : A -> Manner ;             -- 4.2.4 a bare word right after a verb with no object
    VManner : V -> Manner ;                -- 4.2.6 a verb after one that takes no object describes it

    -- slots 8-9: the verb and its objects (4.2, 4.7)
    UseV : V -> VPc ;                      -- 4.2.1 a word as the verb; 4.2.3
    ComplV : V -> NP -> VPc ;              -- 1.2 verb + object
    ComplV3 : V -> NPi -> NP -> VPc ;      -- 4.2.5 recipient, then thing; 5.2.8; 4.6.9 a pause after an open recipient
    ComplV3P : V -> NPi -> NP -> VPc ;     -- 4.6.5 the optional pause between a closed recipient and the thing
    ComplVV : V -> VPa -> VPc ;            -- 4.2.6 the second verb is the object; later phrases go with it
    ComplWun : V -> Cl -> VPc ;            -- 4.8.2 verb + wun clause
    ComplWunMin : V -> Cl -> VPc ;         -- 4.8.5 indirect question: wun bi
    MugeRes : V -> AP -> NP -> VPc ;       -- 4.2.7 muge + result + object: make it so
    GunAP : AP -> VPc ;                    -- 4.7.1 gun + state
    GunNP : NP -> VPc ;                    -- 4.7.2 gun + noun
    GunAdv : Adv -> VPc ;                  -- 4.7.3 gun + place phrase
    GunV : V -> VPc ;                      -- 4.7.4 gun + action word: the undergoer's state
    GunVV : V -> VPa -> VPc ;              -- 12.2, 4.7.4 + 4.2.6: nun gun efon nawi "you are allowed to eat"
    GunWun : Cl -> VPc ;                   -- 4.7.5 gun + wun clause

    -- relation phrases and linked clauses (4.4)
    PrepNP : Prep -> NP -> Adv ;           -- 4.4.1
    PrepCl : Prep -> Cl -> Adv ;           -- 4.4.3 a relation word can take a clause; 12.3 fan + verb
    PrepDrop : Prep -> Adv ;               -- 4.4.2 object dropped: ends its clause or comes before a pause
    SubCl : Sub -> Cl -> Adv ;             -- 4.3.3, 12.1 don/bo + clause
    GiNP : NP -> Adv ;                     -- 4.4.1, 4.8.3 bo + noun phrase "because of": bo yu "why"
                                           -- (at the start, bo win is the linker GiTan only)
    OpAdv : Op -> Adv -> Adv ;             -- 6.2.1 ga mon funti; wan doku su mon guyi
    Mon, Tun, Se, Gan, Li, Ya, Wo, Fu, Nin, Anko, Nuwen : Prep ;   -- 4.4.1, 13.2
    Don, Gi : Sub ;                        -- 4.3.3

    -- quality phrases
    UseA : A -> AP ;                       -- 4.2.3 any word as a quality
    OpAP : Op -> AP -> AP ;                -- 6.2 su upe, ten upe, ke kudu
    CompAP : A -> NP -> AP ;               -- 9.3.4 ke + quality + se + standard
    EquAP : A -> NP -> AP ;                -- 9.3.4 quality + fun + standard: as big as
    RedupA : A -> AP ;                     -- 1.5 doubling strengthens: feko feko
    ModMod : A -> A -> AP ;                -- 5.2.11 tan: the second describing word describes the first (author 2026-10-13)

    -- 5 the noun phrase
    UseN : N -> CN ;                       -- 4.2.3 any word as a noun
    EndearN : N -> CN ;                    -- 5.2.12 fi right after the noun, before its describing words (author 2026-10-15)
    ModCN : CN -> AP -> CN ;               -- 5.2.1 a describing word follows the noun; 5.2.2 gender
    AdvCN : CN -> Prep -> NP -> CN ;       -- 4.4.1 a relation phrase right after a noun may describe it, except fun (manner) (author 2026-10-13)
    DerivV : Deriv -> V -> CN ;            -- 5.4.1 marker + verb
    DerivVP : Deriv -> VPa -> CN ;         -- 5.4.4 marker + verb phrase, to the end of its phrase
    DerivPi : Deriv -> NPi -> CN ;         -- 5.4.6 pu pi mabo
    LannoCN : CN -> CN ;                   -- 10.1.3 lanno before a role or kin word
    Lanno : CN ;                           -- 10.1.3 lanno alone
    No, Ge, Du, Pu : Deriv ;               -- 5.4.2

    QuantCN : CN -> NumOpt -> LaOpt -> DetOpt -> NPq ;  -- 5.1.1 noun, modifiers, number, la, determiner
    PronQ : Pron -> LaOpt -> DetOpt -> NPq ;            -- 10.3.7 wan la; 10.3.6 wan nen; 5.2.8 wan ben
    NameQ : String -> NPq ;                -- 11.1 fo + name (gf_check joins a name's words: it runs to a grammar word or pause)
    NameFi : String -> NPq ;               -- 5.2.12, 11.1 fo + name + fi: fi, a grammar word, ends the name
    NameKiyo : String -> NPq ;             -- 11.1 fo + name + kiyo: a name closed by kiyo may contain grammar words (author 2026-10-13)
    TitleName : CN -> String -> NPq ;      -- 10.1.2 title before the name; 5.4.4
    NumQ : Num -> NPq ;                    -- 5.2.4 a number alone
    DetQ : Det -> NPq ;                    -- 5.2.8 a determiner alone; 4.8.2 yu "what"
    LabelQ : NPq -> Sub100 -> NPq ;        -- 5.2.5, 9.2.3 noun + mena + number: a label (quantity reading)
    LabelDigs : NPq -> Digs -> NPq ;       -- 9.2.3, 8.3.3 larger labels: digit reading
    Clock24 : Digit -> Digit -> Digit -> Digit -> NPq ;  -- 8.3.1 24-hour style
    Clock12 : Sub100 -> Digit -> Digit -> NPq ;          -- 8.3.1 12-hour style: hour, then two digits
    NoNum : NumOpt ;                       -- 5.2.6, 5.2.7
    SomeNum : Num -> NumOpt ;              -- 5.2.5 a count
    AboutNum : Num -> NumOpt ;             -- 9.3.1 fun + number
    HowMany : NumOpt ;                     -- 4.8.3 wifu yu
    NoLa : LaOpt ;                         -- 5.2.6 la is optional
    La : LaOpt ;                           -- 5.2.6
    NoDet : DetOpt ;                       -- 5.2.7 no articles
    SomeDet : Det -> DetOpt ;              -- 5.2.8
    Tan, Ben, We, In, Kin, Fa, Bo, Yu, Mesun, NenD : Det ;   -- 13.1, 5.2.8; 10.3.6 nen "in person"

    PlainNP : NPq -> NPi ;                 -- 5.1.1
    PiNP : NPq -> NPi -> NPi ;             -- 5.2.9 pi + the nearest single noun; 5.2.5 a part (ni pi de)
    RelNP : NPq -> Rel -> NPi ;            -- 5.3.1, 5.3.5 nearest noun; closed by a pause or kiyo
    TimeAnchor : NPq -> Prep -> NPq -> NPi ;  -- 8.2.2, 4.4.1 wuma kon dili ni
    DateNP : NPi -> NPi -> NPi ;           -- 8.3.3, 4.6.8 larger unit, pause, smaller unit
    AboutNP : NPi -> NPi ;                 -- 8.3.1 fun before a time: around noon
    OpNP : Op -> NPi -> NPi ;              -- 6.2.1, 6.2.3 min fo tomas
    UseNPi : NPi -> NP ;                   -- 5.1.1
    ConjNP : NPi -> Conj -> NP -> NP ;     -- 4.4.5 lists
    EitherNP : NPi -> NPi -> NP ;          -- 4.4.5 lu X lu Y
    To, Me, Pen, Din, Wan, Yi, Bu, Sun, Go, Nen : Pron ;   -- 10.3
    NenNen : Pron ;                        -- 1.5 each other
    Yen, Lu, Un : Conj ;                   -- 4.4.5

    -- 5.3 relative clauses
    RelSubj : VP -> Rel ;                  -- 5.3.2, 5.3.8 the noun is the subject
    RelObj : NP -> VPs -> Rel ;            -- 5.3.3 the noun is the object; the subject is kept (5.3.8)
    RelPrep : NP -> VP -> Prep -> Rel ;    -- 5.3.4, 5.3.6 relation word at the end of the clause
    RelWhose : NPq -> VP -> Rel ;          -- 5.3.7 pi wan / pi bun / pi wan la points back to the noun
    SlashV : V -> VPs ;                    -- 5.3.3
    SlashV3 : V -> NPi -> VPs ;            -- 5.3.3 with 4.2.5: the thing is missing after a recipient
    SlashTAM : HabOpt -> AspOpt -> VPs -> VPs ; -- 5.3.3 with 6.2.7, 8.1
    SlashOp : Op -> VPs -> VPs ;           -- 5.3.3 with 6.2.1
    SlashAdv : VPs -> Adv -> VPs ;         -- 5.3.3 with 4.4.1

    -- 9 numbers: the quantity reading (9.2.1) and the digit reading (9.2.2)
    Po, Fi, Sa, Ka, Da, Te, Ufo, Oma, Kefi, Mape : Digit ;   -- 9.1.1
    Units : Digit -> Sub100 ;              -- 0-9
    Tens : Digit -> Sub100 ;               -- 9.2.1 d yawu; a 1 is dropped: yawu
    TensU : Digit -> Digit -> Sub100 ;     -- 9.2.1 yawu ma 15, wo yawu sa 42
    S100 : Sub100 -> Sub1000 ;             -- 9.2.1
    Hund : Digit -> Sub1000 ;              -- 9.2.1 d loki
    HundR : Digit -> Sub100 -> Sub1000 ;   -- 9.2.1 loki ma 105; zero places skipped
    S1000 : Sub1000 -> Num ;               -- 9.2.1
    Thou : Sub1000 -> Num ;                -- 9.2.1 group word munno takes a whole number: sa loki ma yawu munno
    ThouR : Sub1000 -> Sub1000 -> Num ;    -- 9.2.1 group word then the rest
    Thou1 : Num ;                          -- 9.2.1 a 1 before a place word is dropped: munno 1000
    Thou1R : Sub1000 -> Num ;              -- 9.2.1 munno loki ma 1105
    Decimal : Num -> Digs -> Num ;         -- 9.2.4 mimi "point"
    Dg1 : Digit -> Digs ;                  -- 9.2.2 one digit at a time
    DgN : Digs -> Digit -> Digs ;          -- 9.2.2
}
