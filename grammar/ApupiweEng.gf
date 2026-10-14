--# -path=.:alltenses:morphodict
-- English concrete syntax on the RGL. It exists to check glosses (formal-grammar.md check 3), not to
-- translate: a reading's English, bracketed by tools/gf_check.py, sits next to the reference's gloss.
-- A left-out subject shows as "{it}"; a left-out relation object as "{that}".
concrete ApupiweEng of Apupiwe = LexEng ** open SyntaxEng, (P=ParadigmsEng), (E=ExtraEng), (G=GrammarEng),
    (R=ResEng), Prelude in {

  param
    AspT = ASimple | APast | AProg | APastProg | AHabit | ASoon ;
    ActT = AStmt | AQuest | AReq | AInstr | ASub ;
    Mode = MCN | MNP ;

  lincat
    Utt, Sent, Core, Call, Linker, LinkOpt, FrameOpt, CondOpt, Tail, Nun, PMod, ConfOpt, SrcOpt, Sub, Digs,
    Stance = {s : Str} ;
    CallOpt = {first, last : Str} ;
    Act, Part = {t : ActT ; s : Str} ;                 -- s: a note on the act, before the sentence
    Cl, Cl0 = {s : ActT => Str} ;
    VP, VPo = VPr ;
    VPa, VPm, VPc = {vp : SyntaxEng.VP} ;
    VPs = {vps : SyntaxEng.VPSlash ; t : AspT ; neg : Bool} ;
    HabOpt = {hab : Bool} ;
    AspOpt, Asp = {t : AspT} ;
    Op = {neg : Bool ; adv : AdV ; ada : AdA ; s : Str} ;
    Manner = {adv : SyntaxEng.Adv} ;
    AP = {ap : SyntaxEng.AP ; adv : SyntaxEng.Adv} ;
    Adv = SyntaxEng.Adv ;
    Prep = SyntaxEng.Prep ;
    NP, NPi = SyntaxEng.NP ;
    NPq = {cn : SyntaxEng.CN ; det : SyntaxEng.Det ; np : SyntaxEng.NP ; m : Mode} ;
    CN = SyntaxEng.CN ;
    Rel = RS ;
    NumOpt = {e, pl : Bool ; det : SyntaxEng.Det} ;
    LaOpt = {pl : Bool} ;
    DetOpt = {e : Bool ; d : DetR} ;
    Pron = {sg, pl : SyntaxEng.NP} ;
    Det = DetR ;
    Deriv = {head : SyntaxEng.N} ;
    Conj = SyntaxEng.Conj ;
    Digit = {s : Str ; one, z : Bool ; sub10 : G.Sub10 ; dig : G.Digit} ;
    Sub100 = {s, p2 : Str ; one, z : Bool ; n : G.Sub100} ;
    Sub1000 = {s, p3 : Str ; one, z : Bool ; n : G.Sub1000} ;
    Num = {s : Str ; card : Card ; pl, z : Bool} ;   -- the RGL has no zero card: z shows "0" instead

  oper
    VPr : Type = {vp : SyntaxEng.VP ; t : AspT ; neg : Bool ; vps : E.VPS ; conj : Bool} ;
    DetR : Type = {sg, pl : SyntaxEng.Det ; alone : SyntaxEng.NP ; post : Str} ;
    strNP : Str -> SyntaxEng.NP = \s -> lin NP {s = \\_ => s ; a = R.agrP3 R.Sg} ;  -- no inflection: safe for runtime strings
    it0 : SyntaxEng.NP = strNP "{it}" ;
    tns : AspT -> Tense = \t -> case t of {APast | APastProg => pastTense ; _ => presentTense} ;
    pol : Bool -> Pol = \b -> case b of {True => negativePol ; False => positivePol} ;
    vps : SyntaxEng.VP -> AspT -> Bool -> E.VPS = \v,t,n -> E.MkVPS (mkTemp (tns t) simultaneousAnt) (pol n) v ;
    vpr : SyntaxEng.VP -> AspT -> Bool -> VPr = \v,t,n -> {vp = v ; t = t ; neg = n ; vps = vps v t n ; conj = False} ;
    addPre : Str -> SyntaxEng.NP -> SyntaxEng.NP = \p,np -> np ** {s = \\c => p ++ np.s ! c} ;
    addPost : SyntaxEng.NP -> Str -> SyntaxEng.NP = \np,p -> np ** {s = \\c => np.s ! c ++ p} ;
    sAdv : Str -> SyntaxEng.Adv = \s -> P.mkAdv s ;
    clause : SyntaxEng.NP -> Bool -> VPr -> (ActT => Str) = \np,subj,v ->
      let cl = mkCl np v.vp ; t = tns v.t ; p = pol v.neg ;
          plain : Str = case v.conj of {True => (E.PredVPS np v.vps).s ; False => (mkS t p cl).s} in
      table {
        AStmt => plain ;
        ASub => plain ;
        AQuest => case v.conj of {True => plain ++ "?" ; False => (mkUtt (mkQS t p (mkQCl cl))).s ++ "?"} ;
        AReq => case subj of {
          True => "let" ++ (mkUtt np).s ++ (E.UttVPShort v.vp).s ;
          False => "please" ++ (mkUtt p (mkImp v.vp)).s} ;
        AInstr => case subj of {
          True => (mkUtt np).s ++ "," ++ (mkUtt p (mkImp v.vp)).s ;
          False => (mkUtt p (mkImp v.vp)).s}
      } ;
    toNP : {cn : SyntaxEng.CN ; det : SyntaxEng.Det ; np : SyntaxEng.NP ; m : Mode} -> SyntaxEng.NP =
      \q -> case q.m of {MCN => mkNP q.det q.cn ; MNP => q.np} ;
    asNP : SyntaxEng.NP -> {cn : SyntaxEng.CN ; det : SyntaxEng.Det ; np : SyntaxEng.NP ; m : Mode} =
      \np -> {cn = mkCN (P.mkN "") ; det = the_Det ; np = np ; m = MNP} ;
    dt : SyntaxEng.Det -> SyntaxEng.Det -> SyntaxEng.NP -> Str -> DetR =
      \s,p,a,post -> {sg = s ; pl = p ; alone = a ; post = post} ;
    pr : SyntaxEng.NP -> SyntaxEng.NP -> {sg, pl : SyntaxEng.NP} = \s,p -> {sg = s ; pl = p} ;
    part : ActT -> Str -> {t : ActT ; s : Str} = \t,s -> {t = t ; s = s} ;
    op : Bool -> Str -> {neg : Bool ; adv : AdV ; ada : AdA ; s : Str} =
      \n,s -> {neg = n ; adv = P.mkAdV s ; ada = P.mkAdA s ; s = s} ;
    gerund : SyntaxEng.V -> Str = \v -> v.s ! R.VPresPart ;
    who : SyntaxEng.VP -> RS = \v -> mkRS (mkRCl E.who_RP v) ;
    dg : Str -> G.Sub10 -> G.Digit -> Bool -> Bool -> {s : Str ; one, z : Bool ; sub10 : G.Sub10 ; dig : G.Digit} =
      \s,u,d,o,z -> {s = s ; one = o ; z = z ; sub10 = u ; dig = d} ;

  lin
    MkUtt c s t d = {s = c.first ++ s.s ++ t.s ++ d.last} ;
    NoCall = {first, last = []} ;
    SomeCall c = {first = c.s ++ "," ; last = "," ++ c.s} ;
    CallName n = {s = n.s} ;
    CallN n = {s = (mkUtt (mkNP n)).s} ;
    CallLanno = {s = "sir/madam"} ;
    LannoCall c = {s = "honoured" ++ c.s} ;
    NoTail = {s = []} ;
    StanceTail st = {s = "," ++ st.s} ;
    StanceMin st = {s = "," ++ st.s ++ "right?"} ;
    ChoiceYu = {s = "," ++ "which?"} ;
    MinSt = {s = "right?"} ; ASt = {s = "you know"} ; Buni = {s = "okay?"} ; Donon = {s = "it turned out"} ;

    MkSent l f c k = {s = l.s ++ f.s ++ c.s ++ k.s} ;
    NoLink = {s = []} ;
    Link k = {s = k.s ++ ","} ;
    GiTan = {s = "so"} ; UnL = {s = "but"} ; YenL = {s = "also"} ;
    NoFrame = {s = []} ;
    Scene a = {s = (mkUtt a).s ++ ","} ;
    Topic np = {s = "as for" ++ (mkUtt np).s ++ ","} ;
    NoCond = {s = []} ;
    Cond a = {s = (mkUtt a).s ++ ","} ;

    Stmt c = {s = c.s ! AStmt} ;
    ActCl a c = {s = a.s ++ c.s ! a.t} ;
    FragNP np = {s = (mkUtt np).s} ;
    FragAdv a = {s = (mkUtt a).s} ;
    FragAP a = {s = (mkUtt a.ap).s} ;
    PartAct p = p ;
    PartNun p n = {t = p.t ; s = p.s ++ n.s} ;
    NunAct n = {t = AStmt ; s = n.s} ;
    Nun1 = {s = "{politely}"} ; NunNun = {s = "{very politely}"} ;
    MinP = part AQuest [] ; So = part AReq [] ; Tin = part AInstr [] ;
    Fon = part AStmt "{advice}" ; De = part AStmt "{I commit}" ; Yo = part AStmt "{warning}" ;
    BaP = part AStmt "{exclaiming}" ; GensoP = part AStmt "{not literally}" ;
    YoYo = part AStmt "{emergency}" ; GensoGenso = part AStmt "{the whole turn not literally}" ;
    ModPart m p = {t = p.t ; s = m.s ++ p.s} ;
    GensoM = {s = "{not literally}"} ; BaM = {s = "{indignantly}"} ;

    MkCl cf sr c = {s = \\a => cf.s ++ sr.s ++ c.s ! a} ;
    NoConf = {s = []} ; Kon n = {s = "{" ++ n.s ++ "in 6}"} ; KonOf n m = {s = "{" ++ n.s ++ "in" ++ m.s ++ "}"} ; KonBo = {s = "{maybe}"} ;
    NoSrc = {s = []} ; Wanme = {s = "{seen}"} ; Inwun = {s = "{I'm told}"} ; Wemen = {s = "{it seems}"} ;

    PredCl np v = {s = clause np True v} ;
    NoSubj v = {s = clause it0 False v} ;
    ConjCl a c b = {s = \\x => a.s ! x ++ "," ++ c.s2 ++ b.s ! x} ;

    UseVPo v = v ;
    ConjVP a c b = b ** {vps = E.ConjVPS c (E.BaseVPS a.vps b.vps) ; conj = True} ;
    PredVP h a v =
      let v1 : SyntaxEng.VP = case a.t of {AProg | APastProg => progressiveVP v.vp ;
                                           ASoon => mkVP (P.mkAdV "about to") v.vp ;
                                           _ => v.vp} ;
          v2 : SyntaxEng.VP = case h.hab of {True => mkVP (P.mkAdV "usually") v1 ; False => v1} in
      vpr v2 a.t False ;
    OpVP o v = case o.neg of {
      True => vpr v.vp v.t True ;
      False => vpr (mkVP o.adv v.vp) v.t v.neg} ;
    StillNot h v =
      let v1 : SyntaxEng.VP = mkVP (P.mkAdV "yet") v.vp in
      vpr (case h.hab of {True => mkVP (P.mkAdV "usually") v1 ; False => v1}) ASimple True ;
    NoHab = {hab = False} ; Manni = {hab = True} ;
    NoAsp = {t = ASimple} ; SomeAsp a = a ;
    Sin = {t = APast} ; Le = {t = AProg} ; Buntu = {t = ASoon} ; SinLe = {t = APastProg} ;
    Mu = op True [] ; Na = op False "only" ; Fe = op False "also" ; Wi = op False "even" ;
    O = op False "INDEED" ; Konsin = op False "at least" ; Nedin = op False "almost" ;
    Ke = op False "more" ; Bi = op False "very" ; Tason = op False "rather" ;
    MuMu = op True "really" ;

    UseVPm v = v ;
    AdvVP v a = {vp = mkVP v.vp a} ;
    UseVPc v = v ;
    MannerVP v m = {vp = mkVP v.vp m.adv} ;
    BareManner a = {adv = SyntaxEng.mkAdv a} ;
    VManner v = {adv = sAdv (gerund v)} ;

    UseV v = {vp = mkVP v} ;
    ComplV v np = {vp = mkVP (P.mkV2 v) np} ;
    ComplV3 v r t = {vp = mkVP (P.mkV3 v) r t} ;
    ComplV3P v r t = {vp = mkVP (P.mkV3 v) r t} ;
    ComplVV v c = {vp = mkVP (P.mkVV v) c.vp} ;
    ComplWun v c = {vp = mkVP (P.mkVS v) (lin S {s = c.s ! ASub})} ;
    ComplWunMin v c = {vp = mkVP (P.mkVS v) (lin S {s = "whether" ++ c.s ! ASub})} ;
    MugeRes v a np = {vp = mkVP (P.mkV2A v) np a.ap} ;
    GunAP a = {vp = mkVP a.ap} ;
    GunNP np = {vp = mkVP np} ;
    GunAdv a = {vp = mkVP a} ;
    GunV v = {vp = passiveVP (P.mkV2 v)} ;
    GunVV v c = {vp = mkVP (passiveVP (P.mkV2 v)) (sAdv (G.UttVP c.vp).s)} ;
    GunWun c = {vp = mkVP (sAdv ("that" ++ c.s ! ASub))} ;

    PrepNP p np = SyntaxEng.mkAdv p np ;
    PrepCl p c = sAdv (p.s ++ c.s ! ASub) ;
    PrepDrop p = sAdv (p.s ++ "{that}") ;
    SubCl s c = sAdv (s.s ++ c.s ! ASub) ;
    GiNP np = SyntaxEng.mkAdv (P.mkPrep "because of") np ;
    OpAdv o a = sAdv (o.s ++ case o.neg of {True => "not" ; False => []} ++ (mkUtt a).s) ;
    Mon = P.mkPrep "at" ; Tun = to_Prep ; Se = from_Prep ; Gan = with_Prep ; Li = for_Prep ;
    Ya = before_Prep ; Wo = after_Prep ; Fu = P.mkPrep "like" ; Nin = during_Prep ;
    Anko = P.mkPrep "until" ; Nuwen = without_Prep ;
    Don = {s = "if"} ; Gi = {s = "because"} ;

    UseA a = {ap = mkAP a ; adv = SyntaxEng.mkAdv a} ;
    OpAP o a = let ap : SyntaxEng.AP = case o.neg of {True => mkAP (P.mkAdA "not") a.ap ; False => mkAP o.ada a.ap} in
      {ap = ap ; adv = sAdv (mkUtt ap).s} ;
    CompAP a np = let ap = mkAP a np in {ap = ap ; adv = sAdv (mkUtt ap).s} ;
    EquAP a np = let ap = mkAP as_CAdv (mkAP a) np in {ap = ap ; adv = sAdv (mkUtt ap).s} ;
    RedupA a = let ap = mkAP (P.mkAdA "truly") (mkAP a) in {ap = ap ; adv = sAdv (mkUtt ap).s} ;

    UseN n = mkCN n ;
    ModCN cn a = mkCN a.ap cn ;
    AdvCN cn p np = mkCN cn (SyntaxEng.mkAdv p np) ;
    DerivV d v = mkCN (mkCN d.head) (who (mkVP v)) ;
    DerivVP d v = mkCN (mkCN d.head) (who v.vp) ;
    DerivPi d n = mkCN (mkCN d.head) (SyntaxEng.mkAdv possess_Prep n) ;
    LannoCN cn = mkCN (P.mkA "honoured") cn ;
    Lanno = mkCN (P.mkN "honoured one") ;
    No = {head = P.mkN "one"} ; Ge = {head = P.mkN "thing"} ; Du = {head = P.mkN "tool"} ; Pu = {head = P.mkN "place"} ;

    QuantCN cn n l d =
      let pl : Bool = orB l.pl n.pl in
      case d.e of {
        False => {cn = cn ; det = case pl of {True => d.d.pl ; False => d.d.sg} ; np = d.d.alone ; m = MCN} ;
        True => case n.e of {
          False => {cn = cn ; det = n.det ; np = it0 ; m = MCN} ;
          True => {cn = cn ; det = case l.pl of {True => thePl_Det ; False => the_Det} ; np = it0 ; m = MCN}}} ;
    PronQ p l d = asNP (case d.e of {
      True => case l.pl of {True => p.pl ; False => p.sg} ;
      False => addPost (case l.pl of {True => p.pl ; False => p.sg}) d.d.post}) ;
    NameQ n = asNP (strNP n.s) ;
    TitleName cn n = asNP (mkNP (mkCN cn (strNP n.s))) ;
    NumQ n = asNP (case n.z of {True => strNP "0" ; False => mkNP (mkDet n.card)}) ;
    DetQ d = asNP d.alone ;
    LabelQ q n = q ** {cn = mkCN q.cn (strNP n.s) ; np = addPost q.np n.s} ;
    LabelDigs q n = q ** {cn = mkCN q.cn (strNP n.s) ; np = addPost q.np n.s} ;
    Clock24 a b c d = asNP (strNP (a.s ++ BIND ++ b.s ++ BIND ++ ":" ++ BIND ++ c.s ++ BIND ++ d.s)) ;
    Clock12 h a b = asNP (strNP (h.s ++ BIND ++ ":" ++ BIND ++ a.s ++ BIND ++ b.s)) ;
    NoNum = {e = True ; pl = False ; det = the_Det} ;
    SomeNum n = {e = False ; pl = n.pl ; det = mkDet n.card} ;
    AboutNum n = {e = False ; pl = True ; det = mkDet (mkCard (P.mkAdN "about") n.card)} ;
    HowMany = {e = False ; pl = True ; det = mkDet (P.mkQuant "how many" "how many") pluralNum} ;
    NoLa = {pl = False} ; La = {pl = True} ;
    NoDet = {e = True ; d = Tan} ; SomeDet d = {e = False ; d = d} ;
    Tan = dt this_Det these_Det this_NP [] ;
    Ben = dt that_Det those_Det that_NP [] ;
    We = dt every_Det thePl_Det (strNP "all") [] ;
    In = dt someSg_Det somePl_Det (strNP "some") [] ;
    Kin = dt somePl_Det somePl_Det (strNP "some, not all") [] ;
    Fa = dt (mkDet no_Quant) (mkDet no_Quant pluralNum) (strNP "none") [] ;
    Bo = dt someSg_Det somePl_Det something_NP [] ;
    Yu = dt (mkDet (P.mkQuant "which" "which")) (mkDet (P.mkQuant "which" "which") pluralNum) (strNP "what") [] ;
    Mesun = dt every_Det every_Det everybody_NP [] ;
    NenD = dt the_Det thePl_Det (strNP "oneself") "in person" ;

    PlainNP q = toNP q ;
    PiNP q n = case q.m of {
      MCN => mkNP q.det (mkCN q.cn (SyntaxEng.mkAdv possess_Prep n)) ;
      MNP => mkNP q.np (SyntaxEng.mkAdv possess_Prep n)} ;
    RelNP q r = case q.m of {
      MCN => mkNP q.det (mkCN q.cn r) ;
      MNP => mkNP q.np r} ;
    TimeAnchor a p o = mkNP (toNP o) (SyntaxEng.mkAdv p (toNP a)) ;
    DateNP a b = strNP ((mkUtt a).s ++ "," ++ (mkUtt b).s) ;
    AboutNP n = addPre "about" n ;
    OpNP o n = addPre (case o.neg of {True => "not" ; False => o.s}) n ;
    UseNPi n = n ;
    ConjNP a c b = mkNP c a b ;
    EitherNP a b = mkNP either7or_DConj a b ;
    To = pr i_NP we_NP ; Me = pr you_NP youPl_NP ; Pen = pr we_NP we_NP ; Din = pr we_NP we_NP ;
    Wan = pr she_NP they_NP ; Yi = pr he_NP they_NP ; Bu = pr it_NP they_NP ; Sun = pr he_NP they_NP ;
    Go = pr everybody_NP everybody_NP ;
    Nen = pr (strNP "oneself") (strNP "themselves") ;
    NenNen = pr (strNP "each other") (strNP "each other") ;
    Yen = and_Conj ; Lu = or_Conj ; Un = P.mkConj "but" ;

    RelSubj v = mkRS (tns v.t) (pol v.neg) (mkRCl E.who_RP v.vp) ;
    RelObj np v = mkRS (tns v.t) (pol v.neg) (mkRCl E.that_RP (mkClSlash np v.vps)) ;
    RelPrep np v p = mkRS (tns v.t) (pol v.neg) (mkRCl E.that_RP (mkClSlash (mkCl np v.vp) p)) ;
    RelWhose q v = lin RS {s = \\_ => "whose" ++ (mkS (tns v.t) (pol v.neg) (mkCl (mkNP q.cn) v.vp)).s ; c = R.npNom} ;
    SlashV v = {vps = mkVPSlash (P.mkV2 v) ; t = ASimple ; neg = False} ;
    SlashV3 v r = {vps = mkVPSlash (P.mkV3 v) r ; t = ASimple ; neg = False} ;
    SlashTAM h a v = v ** {t = a.t} ;
    SlashOp o v = v ** {neg = orB o.neg v.neg} ;
    SlashAdv v a = v ** {vps = G.AdvVPSlash v.vps a} ;

    Po = dg "0" G.pot01 G.n2 False True ; Fi = dg "1" G.pot01 G.n2 True False ;
    Sa = dg "2" (G.pot0 G.n2) G.n2 False False ; Ka = dg "3" (G.pot0 G.n3) G.n3 False False ;
    Da = dg "4" (G.pot0 G.n4) G.n4 False False ; Te = dg "5" (G.pot0 G.n5) G.n5 False False ;
    Ufo = dg "6" (G.pot0 G.n6) G.n6 False False ; Oma = dg "7" (G.pot0 G.n7) G.n7 False False ;
    Kefi = dg "8" (G.pot0 G.n8) G.n8 False False ; Mape = dg "9" (G.pot0 G.n9) G.n9 False False ;
    Units d = {s = d.s ; p2 = "0" ++ BIND ++ d.s ; one = d.one ; z = d.z ; n = G.pot0as1 d.sub10} ;
    Tens d = let s = d.s ++ BIND ++ "0" in
      {s = s ; p2 = s ; one = False ; z = False ; n = case d.one of {True => G.pot110 ; False => G.pot1 d.dig}} ;
    TensU d u = let s = d.s ++ BIND ++ u.s in
      {s = s ; p2 = s ; one = False ; z = False ;
       n = case d.one of {
         True => case u.one of {True => G.pot111 ; False => G.pot1to19 u.dig} ;
         False => G.pot1plus d.dig u.sub10}} ;
    S100 n = {s = n.s ; p3 = "0" ++ BIND ++ n.p2 ; one = n.one ; z = n.z ; n = G.pot1as2 n.n} ;
    Hund d = let s = d.s ++ BIND ++ "00" in {s = s ; p3 = s ; one = False ; z = False ; n = G.pot2 d.sub10} ;
    HundR d r = let s = d.s ++ BIND ++ r.p2 in {s = s ; p3 = s ; one = False ; z = False ; n = G.pot2plus d.sub10 r.n} ;
    S1000 n = {s = n.s ; pl = notB n.one ; z = n.z ; card = mkCard (G.num (G.pot2as3 n.n))} ;
    Thou n = {s = n.s ++ BIND ++ "000" ; pl = True ; z = False ; card = mkCard (G.num (G.pot3 n.n))} ;
    ThouR n r = {s = n.s ++ BIND ++ r.p3 ; pl = True ; z = False ; card = mkCard (G.num (G.pot3plus n.n r.n))} ;
    Thou1 = {s = "1000" ; pl = True ; z = False ; card = mkCard (G.num (G.pot3 (G.pot1as2 (G.pot0as1 G.pot01))))} ;
    Thou1R r = {s = "1" ++ BIND ++ r.p3 ; pl = True ; z = False ;
                card = mkCard (G.num (G.pot3plus (G.pot1as2 (G.pot0as1 G.pot01)) r.n))} ;
    Decimal n d = {s = n.s ++ BIND ++ "." ++ BIND ++ d.s ; pl = True ; z = False ; card = n.card} ;
    Dg1 d = {s = d.s} ;
    DgN ds d = {s = ds.s ++ BIND ++ d.s} ;
}
