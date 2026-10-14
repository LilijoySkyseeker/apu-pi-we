-- Apupiwe concrete syntax. Words never change form (2.5), so every phrase is a string plus a few flags
-- that let the grammar, not a post-filter, enforce the reference's attachment and pause rules:
--   e   how the phrase ends. An open ending (a relative clause or phrasal derived word, ER/ED; a clause
--       or a relation word with its object dropped, EC) swallows whatever follows, so anything attached
--       after it from outside needs a pause (or kiyo, for ER/ED) first (1.4, 4.4.4, 4.6.9, 5.3.5, 5.4.4).
--   p   the phrase holds such a closing pause; a pause or kiyo closes every relative clause still open
--       (5.3.5), so a phrase with p can't be a relative clause's or a derived word's body.
--   other flags are explained where they are set.
concrete ApupiweApu of Apupiwe = LexApu ** open Prelude in {

  param
    End = EV    -- ends in a verb, quality or grammar word
        | EN    -- ends in a closed noun phrase
        | EG    -- ends in a gender word (5.4.4)
        | EM    -- ends in a name (5.4.4)
        | ER    -- ends in an open relative clause (5.3.5)
        | ED    -- ends in an open phrasal derived word (5.4.4)
        | EC ;  -- ends in an open clause or a dropped relation object (4.4.2, 4.4.4)

  lincat
    Utt, Sent, Core, Call, Linker, Act, PMod, Nun, Sub, Pron, Deriv, Conj, Asp, Num,
    FrameOpt, CondOpt, LinkOpt, Tail, ConfOpt, SrcOpt = SS ;
    CallOpt = {first, last : Str} ;
    Part = {s : Str ; m : Bool} ;                 -- m: already modified (7.1.3)
    Stance = {s : Str ; m : Bool} ;               -- m: it is min (7.2.7)
    Op = {s : Str ; ke : Bool} ;                  -- ke: the comparative degree word (9.3.4)
    HabOpt, AspOpt, NumOpt, LaOpt = {s : Str ; e : Bool} ;   -- e: empty
    DetOpt = {s : Str ; e, al : Bool} ;           -- al: the determiner may stand alone
    Det = {s : Str ; alone : Bool} ;              -- alone: may stand alone as a noun phrase (5.2.8)
    Prep = {s : Str ; wy, se, cd, mn : Bool} ;    -- wo/ya (4.4.1); se (9.3.4); takes an if/when clause (4.3.3); mn: fu, the manner word (4.4.1)
    Digit = {s, mul : Str ; z, one, small : Bool} ;   -- mul: before a place word (a 1 is dropped, 9.2.1)
    Sub100 = {s : Str ; z, one, hr : Bool} ;      -- hr: 1-12, an hour (8.3.1)
    Sub1000 = {s : Str ; z, one : Bool} ;
    Digs = {s : Str ; n2, n3 : Bool} ;            -- at least 2, 3 digits
    Rel, VPs = Ph ;
    Cl, Cl0 = {s : Str ; e : End ; p : Bool ; sj : Bool} ;   -- sj: has a subject
    VP, VPo, VPa, VPm = {s : Str ; e : End ; p : Bool ; et, ek, w1, vv : Bool} ;
      -- et: ends in a time phrase; ek: ends in a ke-comparative without its standard; w1: a single verb
      -- vv: ends in a verb that is the object of the verb before it, so later phrases go with it (4.2.6)
    VPc = {s : Str ; e : End ; p : Bool ; et, ek, bare, tobj, vv : Bool} ;
      -- bare: the verb alone; tobj: the verb takes an object (4.2.6)
    Manner = {s : Str ; e : End ; p : Bool ; vm : Bool} ;
      -- follows only a verb with no object (4.2.4); vm: a verb describing a verb (4.2.6)
    AP = {s : Str ; e : End ; p : Bool ; act, ek, gd : Bool} ;
      -- act: a bare action root (4.7.4); gd: a gender word (5.4.4)
    Adv = {s : Str ; e : End ; p : Bool ; et, wy, sc, cd, se : Bool} ;
      -- sc: may set the scene (4.3.1); cd: an if/when clause (4.3.3)
    CN = {s : Str ; e : End ; p : Bool ; tm, ba, w1 : Bool} ;   -- w1: a single bare root
      -- tm: a time phrase (4.4.1, 8.2); ba: headed by an action root, so gun + it is the undergoer's state (4.7.4)
    NP, NPi, NPq = {s : Str ; e : End ; p : Bool ; tm, ba, dt, ns, hn, cnt, rs : Bool} ;
      -- rs: a bare root + a determiner or number that could stand alone: after muge, a result + object (4.2.7)
      -- dt: a determiner standing alone (5.2.8); ns: starts with a number; hn: headed by a noun or pronoun (5.2.5);
      -- cnt: ends in a bare noun or a number, so a number right after it is its count (5.2.5, 9.2.1)

  oper
    Ph : Type = {s : Str ; e : End ; p : Bool} ;
    opn : End -> Bool = \e -> case e of {ER | ED | EC => True ; _ => False} ;
    nounEnd : End -> Bool = \e -> case e of {EN | EG | EM => True ; _ => False} ;
    -- the pause (or kiyo) that closes an open ending before more material (4.6.9, 5.3.5)
    closer : End -> Str = \e -> case e of {ER | ED => "," | "kiyo" ; EC => "," ; _ => []} ;
    -- x, then material that attaches outside x
    seq : Ph -> Str -> Str = \x,r -> x.s ++ closer x.e ++ r ;
    -- the closing-pause flag of x followed by something with flag b
    pz : Ph -> Bool -> Bool = \x,b -> orB (orB x.p (opn x.e)) b ;
    -- the pause between joined clauses or verbs: required when the first ends in a noun (4.6.6)
    joinPause : End -> Str = \e -> case e of {EN | EG | EM | EC => "," ; ER | ED => "," | "kiyo" ; EV => []} ;
    joinP : Ph -> Bool -> Bool = \x,b -> orB (orB x.p (orB (opn x.e) (nounEnd x.e))) b ;
    no : {s : Str} = {s = Predef.nonExist} ;
    vpa : Str -> End -> Bool -> Bool -> Bool -> {s : Str ; e : End ; p : Bool ; et, ek, w1, vv : Bool} =
      \s,e,p,et,ek -> {s = s ; e = e ; p = p ; et = et ; ek = ek ; w1 = False ; vv = False} ;
    vpc : Str -> End -> Bool -> Bool -> Bool -> Bool -> {s : Str ; e : End ; p : Bool ; et, ek, bare, tobj, vv : Bool} =
      \s,e,p,et,ek,t -> {s = s ; e = e ; p = p ; et = et ; ek = ek ; bare = False ; tobj = t ; vv = False} ;
    npr : Str -> End -> Bool -> Bool -> {s : Str ; e : End ; p : Bool ; tm, ba, dt, ns, hn, cnt, rs : Bool} =
      \s,e,p,tm -> {s = s ; e = e ; p = p ; tm = tm ; ba = False ; dt = False ; ns = False ; hn = True ; cnt = False ; rs = False} ;
    gend : Bool -> End = \g -> case g of {True => EG ; False => EV} ;
    adv : Str -> End -> Bool -> {s : Str ; e : End ; p : Bool ; et, wy, sc, cd, se : Bool} =
      \s,e,p -> {s = s ; e = e ; p = p ; et = False ; wy = False ; sc = False ; cd = False ; se = False} ;
    nonEx : {s : Str ; e : End ; p : Bool ; et, wy, sc, cd, se : Bool} = adv Predef.nonExist EV False ;
    prep : Str -> Bool -> Bool -> Bool -> {s : Str ; wy, se, cd, mn : Bool} = \s,w,se,c -> {s = s ; wy = w ; se = se ; cd = c ; mn = False} ;
    dg : Str -> Bool -> Bool -> Bool -> {s, mul : Str ; z, one, small : Bool} =
      \s,z,o,sm -> {s = s ; mul = case o of {True => [] ; False => s} ; z = z ; one = o ; small = sm} ;
    tens : {mul : Str} -> Str = \d -> d.mul ++ "yawu" ;
    hund : {mul : Str} -> Str = \d -> d.mul ++ "loki" ;
    op : Str -> {s : Str ; ke : Bool} = \s -> {s = s ; ke = False} ;

  lin
    -- 4.1 the template
    MkUtt c s t d = ss (c.first ++ s.s ++ t.s ++ d.last) ;
    NoCall = {first, last = []} ;
    SomeCall c = {first = c.s ++ "," ; last = "," ++ c.s} ;
    CallName n = ss ("en" ++ n.s) ;
    CallN n = ss n.s ;
    CallLanno = ss "lanno" ;
    LannoCall c = ss ("lanno" ++ c.s) ;
    NoTail = ss [] ;
    StanceTail st = ss ("," ++ st.s) ;
    StanceMin st = case st.m of {True => no ; False => ss ("," ++ st.s ++ "min")} ;
    ChoiceYu = ss ("," ++ "yu") ;
    MinSt = {s = "min" ; m = True} ; ASt = {s = "a" ; m = False} ;
    Buni = {s = "buni" ; m = False} ; Donon = {s = "donon" ; m = False} ;

    MkSent l f c k = ss (l.s ++ f.s ++ c.s ++ k.s) ;
    NoLink = ss [] ;
    Link k = ss (k.s ++ ",") ;
    GiTan = ss ("gi" ++ "tan") ; UnL = ss "un" ; YenL = ss "yen" ;
    NoFrame = ss [] ;
    Scene a = case a.sc of {True => ss (a.s ++ ",") ; False => no} ;
    Topic np = case np.p of {False => ss ("pi" ++ np.s ++ ("," | "kiyo")) ; True => no} ;
    NoCond = ss [] ;
    Cond a = case a.cd of {True => ss (a.s ++ ",") ; False => no} ;

    Stmt c = ss c.s ;
    ActCl a c = ss (a.s ++ c.s) ;
    FragNP np = ss np.s ;
    FragAdv a = ss a.s ;
    FragAP a = ss a.s ;
    PartAct p = ss p.s ;
    PartNun p n = ss (p.s ++ n.s) ;
    NunAct n = n ;
    Nun1 = ss "nun" ; NunNun = ss ("nun" ++ "nun") ;
    MinP = {s = "min" ; m = False} ; So = {s = "so" ; m = False} ; Tin = {s = "tin" ; m = False} ;
    Fon = {s = "fon" ; m = False} ; De = {s = "de" ; m = False} ; Yo = {s = "yo" ; m = False} ;
    BaP = {s = "ba" ; m = True} ; GensoP = {s = "genso" ; m = True} ;
    YoYo = {s = "yo" ++ "yo" ; m = True} ; GensoGenso = {s = "genso" ++ "genso" ; m = True} ;
    ModPart pm p = case p.m of {True => {s = Predef.nonExist ; m = True} ; False => {s = pm.s ++ p.s ; m = True}} ;
    GensoM = ss "genso" ; BaM = ss "ba" ;

    MkCl cf sr c = c ** {s = cf.s ++ sr.s ++ c.s} ;
    NoConf = ss [] ; Kon n = ss ("kon" ++ n.s) ; KonOf n m = ss ("kon" ++ n.s ++ "pi" ++ m.s) ; KonBo = ss ("kon" ++ "bo") ;
    NoSrc = ss [] ; Wanme = ss "wanme" ; Inwun = ss "inwun" ; Wemen = ss "wemen" ;

    PredCl np vp = {s = seq np vp.s ; e = vp.e ; p = pz np vp.p ; sj = True} ;
    NoSubj vp = {s = vp.s ; e = vp.e ; p = vp.p ; sj = False} ;
    ConjCl a c b = case b.sj of {
      True => {s = a.s ++ joinPause a.e ++ c.s ++ b.s ; e = b.e ; p = joinP a b.p ; sj = a.sj} ;
      False => {s = Predef.nonExist ; e = EV ; p = False ; sj = False}} ;

    UseVPo v = v ;
    ConjVP a c b = vpa (a.s ++ joinPause a.e ++ c.s ++ b.s) b.e (joinP a b.p) b.et b.ek ;
    PredVP h a v = case <h.e, a.e> of {
      <True, True> => v ** {s = h.s ++ a.s ++ v.s} ;
      _ => v ** {s = h.s ++ a.s ++ v.s ; w1 = False}} ;
    OpVP o v = v ** {s = o.s ++ v.s ; w1 = False} ;
    StillNot h v = v ** {s = h.s ++ "le" ++ "mu" ++ v.s ; w1 = False} ;
    NoHab = {s = [] ; e = True} ; Manni = {s = "manni" ; e = False} ;
    NoAsp = {s = [] ; e = True} ; SomeAsp a = {s = a.s ; e = False} ;
    Sin = ss "sin" ; Le = ss "le" ; Buntu = ss "buntu" ; SinLe = ss ("sin" ++ "le") ;
    Mu = op "mu" ; Na = op "na" ; Fe = op "fe" ; Wi = op "wi" ; O = op "o" ;
    Konsin = op "konsin" ; Nedin = op "nedin" ;
    Ke = {s = "ke" ; ke = True} ; Bi = op "bi" ; Tason = op "tason" ;
    MuMu = op ("mu" ++ "mu") ;

    UseVPm v = v ;
    -- 4.4.1: after a time, wo and ya belong to that time; 9.3.4: after ke + quality, se is its standard
    -- 4.2.6: after a verb that is the object of the verb before it, phrases go with that verb (ComplVV)
    AdvVP v a = case <a.wy, v.et, a.se, v.ek, v.vv> of {
      <True, True, _, _, _> => vpa Predef.nonExist EV False False False ;
      <_, _, True, True, _> => vpa Predef.nonExist EV False False False ;
      <_, _, _, _, True> => vpa Predef.nonExist EV False False False ;
      _ => vpa (seq v a.s) a.e (pz v a.p) a.et False} ;
    UseVPc v = {s = v.s ; e = v.e ; p = v.p ; et = v.et ; ek = v.ek ; w1 = v.bare ; vv = v.vv} ;
    MannerVP v m = case <v.bare, m.vm, v.tobj> of {
      <False, _, _> => vpa Predef.nonExist EV False False False ;
      <_, True, True> => vpa Predef.nonExist EV False False False ;
      _ => vpa (seq v m.s) m.e (pz v m.p) False False} ;
    BareManner a = {s = a.s ; e = gend a.gd ; p = False ; vm = False} ;
    VManner v = {s = v.s ; e = gend v.gd ; p = False ; vm = True} ;

    -- et: wo/ya after a time word belong to it (4.4.1), whatever its role
    UseV v = {s = v.s ; e = gend v.gd ; p = False ; et = v.tm ; ek = False ; bare = True ; tobj = v.obj ; vv = False} ;
    ComplV v np = case andB v.res np.rs of {
      False => vpc (v.s ++ np.s) np.e np.p np.tm False v.obj ;
      True => vpc Predef.nonExist EV False False False False} ;
    -- 5.2.8: a determiner right after a noun belongs to it; 5.2.5: so does a number (its count)
    ComplV3 v r t = case <t.dt, andB t.ns r.cnt> of {
      <False, False> => vpc (v.s ++ seq r t.s) t.e (pz r t.p) t.tm False v.obj ;
      _ => vpc Predef.nonExist EV False False False False} ;
    -- 4.6.5: a pause between a closed recipient and the thing is optional (an open one needs it: ComplV3)
    ComplV3P v r t = case <opn r.e, t.dt> of {
      <False, False> => vpc (v.s ++ r.s ++ "," ++ t.s) t.e True t.tm False v.obj ;
      _ => vpc Predef.nonExist EV False False False False} ;
    ComplVV v c = case v.obj of {
      True => (vpc (v.s ++ c.s) c.e c.p c.et c.ek v.obj) ** {vv = True} ;
      False => vpc Predef.nonExist EV False False False False} ;
    ComplWun v c = vpc (v.s ++ "wun" ++ c.s) EC c.p False False v.obj ;
    ComplWunMin v c = vpc (v.s ++ "wun" ++ "min" ++ c.s) EC c.p False False v.obj ;
    MugeRes v a np = case v.res of {
      True => vpc (v.s ++ seq a np.s) np.e (pz a np.p) np.tm False True ;
      False => vpc Predef.nonExist EV False False False False} ;
    GunAP a = case a.act of {
      False => vpc ("gun" ++ a.s) a.e a.p False a.ek False ;
      True => vpc Predef.nonExist EV False False False False} ;
    GunNP np = case np.ba of {
      False => vpc ("gun" ++ np.s) np.e np.p np.tm False False ;
      True => vpc Predef.nonExist EV False False False False} ;
    GunAdv a = case a.sc of {
      True => vpc ("gun" ++ a.s) a.e a.p a.et False False ;
      False => vpc Predef.nonExist EV False False False False} ;
    GunV v = case v.act of {
      True => vpc ("gun" ++ v.s) EV False False False False ;
      False => vpc Predef.nonExist EV False False False False} ;
    GunVV v c = case <v.act, v.obj> of {
      <True, True> => (vpc ("gun" ++ v.s ++ c.s) c.e c.p c.et c.ek False) ** {vv = True} ;
      _ => vpc Predef.nonExist EV False False False False} ;
    GunWun c = vpc ("gun" ++ "wun" ++ c.s) EC c.p False False False ;

    PrepNP pr np = {s = pr.s ++ np.s ; e = np.e ; p = np.p ; et = np.tm ; wy = pr.wy ; sc = True ; cd = False ; se = pr.se} ;
    PrepCl pr c = {s = pr.s ++ c.s ; e = EC ; p = c.p ; et = False ; wy = pr.wy ; sc = notB pr.cd ; cd = pr.cd ; se = pr.se} ;
    PrepDrop pr = {s = pr.s ; e = EC ; p = False ; et = False ; wy = pr.wy ; sc = True ; cd = False ; se = pr.se} ;
    SubCl sb c = (adv (sb.s ++ c.s) EC c.p) ** {cd = True} ;
    GiNP np = adv ("gi" ++ np.s) np.e np.p ;
    OpAdv o a = a ** {s = o.s ++ a.s} ;
    Mon = prep "mon" False False False ; Tun = prep "tun" False False False ;
    Se = prep "se" False True False ; Gan = prep "gan" False False False ;
    Li = prep "li" False False False ; Ya = prep "ya" True False True ;
    Wo = prep "wo" True False True ; Fu = (prep "fu" False False False) ** {mn = True} ;
    Nin = prep "nin" False False True ; Anko = prep "anko" False False False ;
    Nuwen = prep "nuwen" False False False ;
    Don = ss "don" ; Gi = ss "gi" ;

    UseA a = {s = a.s ; e = gend a.gd ; p = False ; act = a.act ; ek = False ; gd = a.gd} ;
    OpAP o a = {s = o.s ++ a.s ; e = a.e ; p = a.p ; act = False ; ek = o.ke ; gd = False} ;
    CompAP a np = {s = "ke" ++ a.s ++ "se" ++ np.s ; e = np.e ; p = np.p ; act = False ; ek = False ; gd = False} ;
    EquAP a np = {s = a.s ++ "fu" ++ np.s ; e = np.e ; p = np.p ; act = a.act ; ek = False ; gd = False} ;
    RedupA a = {s = a.s ++ a.s ; e = EV ; p = False ; act = a.act ; ek = False ; gd = False} ;

    UseN n = {s = n.s ; e = case n.gd of {True => EG ; False => EN} ; p = False ; tm = n.tm ; ba = n.act ; w1 = True} ;
    -- 5.4.4: a gender word after a phrasal derived word is outside it, with no pause
    ModCN cn a =
      let e : End = case a.gd of {True => EG ; False => case opn a.e of {True => a.e ; False => EN}} in
      case <cn.e, a.gd> of {
        <ED, True> => {s = cn.s ++ a.s ; e = e ; p = orB cn.p a.p ; tm = cn.tm ; ba = cn.ba ; w1 = False} ;
        _ => {s = seq cn a.s ; e = e ; p = pz cn a.p ; tm = cn.tm ; ba = cn.ba ; w1 = False}} ;
    -- 4.4.1 (2026-10-13): a relation phrase right after a noun may describe it; not fu, which after an object
    -- marks manner (4.2.4); not after a pronoun (pronouns aren't CN); not a time noun + wo/ya (TimeAnchor)
    AdvCN cn pr np = case orB pr.mn (andB cn.tm pr.wy) of {
      False => {s = seq cn (pr.s ++ np.s) ; e = np.e ; p = pz cn np.p ; tm = cn.tm ; ba = cn.ba ; w1 = False} ;
      True => {s = Predef.nonExist ; e = EV ; p = False ; tm = False ; ba = False ; w1 = False}} ;
    DerivV d v = {s = d.s ++ v.s ; e = EN ; p = False ; tm = False ; ba = False ; w1 = False} ;
    -- 5.4.4: a phrasal base runs to the end of its phrase, but ends before a name or a gender word;
    -- a single verb is DerivV
    DerivVP d v = case <v.w1, v.p, v.e> of {
      <False, False, EV | EN> => {s = d.s ++ v.s ; e = ED ; p = False ; tm = False ; ba = False ; w1 = False} ;
      <False, False, ER | EC> => {s = d.s ++ v.s ; e = v.e ; p = False ; tm = False ; ba = False ; w1 = False} ;
      _ => {s = Predef.nonExist ; e = EV ; p = False ; tm = False ; ba = False ; w1 = False}} ;
    DerivPi d np = {s = d.s ++ "pi" ++ np.s ; e = np.e ; p = np.p ; tm = False ; ba = False ; w1 = False} ;
    LannoCN cn = cn ** {s = "lanno" ++ cn.s ; ba = False ; w1 = False} ;
    Lanno = {s = "lanno" ; e = EN ; p = False ; tm = False ; ba = False ; w1 = False} ;
    No = ss "no" ; Ge = ss "ge" ; Du = ss "du" ; Pu = ss "pu" ;

    QuantCN cn n l d = case <n.e, l.e, d.e> of {
      <True, True, True> => {s = cn.s ++ n.s ++ l.s ++ d.s ; e = cn.e ; p = cn.p ; tm = cn.tm ; ba = cn.ba ; dt = False ; ns = False ; hn = True ; cnt = True ; rs = False} ;
      _ => {s = seq cn (n.s ++ l.s ++ d.s) ; e = EN ; p = pz cn False ; tm = cn.tm ; ba = cn.ba ; dt = False ; ns = False ; hn = True ; cnt = andB l.e d.e ;
            rs = andB cn.w1 (andB l.e (orB (andB n.e d.al) (andB (notB n.e) d.e)))}} ;
    PronQ pr l d = npr (pr.s ++ l.s ++ d.s) EN False False ;
    NameQ n = npr ("en" ++ n.s) EM False False ;
    TitleName cn n = case cn.e of {
      ER | EC => npr Predef.nonExist EV False False ;
      _ => npr (cn.s ++ "en" ++ n.s) EM cn.p False} ;
    NumQ n = (npr n.s EN False False) ** {ns = True ; hn = False ; cnt = True} ;
    DetQ d = case d.alone of {
      True => (npr d.s EN False False) ** {dt = True ; hn = False} ;
      False => npr Predef.nonExist EV False False} ;
    LabelQ q n = case q.hn of {
      True => q ** {s = seq q ("mena" ++ n.s) ; e = EN ; p = pz q False ; cnt = True} ;
      False => npr Predef.nonExist EV False False} ;
    LabelDigs q n = case <q.hn, n.n3> of {
      <True, True> => q ** {s = seq q ("mena" ++ n.s) ; e = EN ; p = pz q False ; cnt = True} ;
      _ => npr Predef.nonExist EV False False} ;
    Clock24 a b c d = (npr (a.s ++ b.s ++ c.s ++ d.s) EN False True) ** {ns = True} ;
    Clock12 h a b = case h.hr of {
      True => (npr (h.s ++ a.s ++ b.s) EN False True) ** {ns = True} ;
      False => npr Predef.nonExist EV False False} ;
    NoNum = {s = [] ; e = True} ;
    SomeNum n = {s = n.s ; e = False} ;
    AboutNum n = {s = "fu" ++ n.s ; e = False} ;
    HowMany = {s = "wifu" ++ "yu" ; e = False} ;
    NoLa = {s = [] ; e = True} ; La = {s = "la" ; e = False} ;
    NoDet = {s = [] ; e = True ; al = False} ; SomeDet d = {s = d.s ; e = False ; al = d.alone} ;
    Tan = {s = "tan" ; alone = True} ; Ben = {s = "ben" ; alone = True} ; We = {s = "we" ; alone = True} ;
    In = {s = "in" ; alone = True} ; Kin = {s = "kin" ; alone = True} ; Fa = {s = "fa" ; alone = True} ;
    Bo = {s = "bo" ; alone = False} ; Yu = {s = "yu" ; alone = True} ; Mesun = {s = "mesun" ; alone = False} ;
    NenD = {s = "nen" ; alone = False} ;

    PlainNP q = q ;
    PiNP q n = q ** {s = seq q ("pi" ++ n.s) ; e = n.e ; p = pz q n.p ; cnt = n.cnt} ;
    RelNP q r = case r.p of {
      False => q ** {s = seq q r.s ; e = ER ; p = pz q False ; tm = False ; cnt = False} ;
      True => npr Predef.nonExist EV False False} ;
    TimeAnchor a pr o = case <a.tm, pr.wy> of {
      <True, True> => (npr (seq a (pr.s ++ o.s)) o.e (pz a o.p) True) ** {dt = a.dt ; ns = a.ns ; hn = a.hn ; cnt = o.cnt} ;
      _ => npr Predef.nonExist EV False False} ;
    DateNP a b = case <a.tm, b.tm> of {
      <True, True> => b ** {s = a.s ++ "," ++ b.s ; p = True ; ns = a.ns ; hn = a.hn ; dt = a.dt} ;
      _ => npr Predef.nonExist EV False False} ;
    AboutNP n = case n.tm of {
      True => n ** {s = "fu" ++ n.s ; ba = False ; dt = False ; ns = False} ;
      False => npr Predef.nonExist EV False False} ;
    OpNP o n = n ** {s = o.s ++ n.s ; ba = False ; dt = False ; ns = False} ;
    UseNPi n = n ;
    ConjNP a c b = b ** {s = seq a (c.s ++ b.s) ; p = pz a b.p ; tm = False ; ba = a.ba ; dt = a.dt ; ns = a.ns ; hn = a.hn} ;
    EitherNP a b = b ** {s = "lu" ++ seq a ("lu" ++ b.s) ; p = pz a b.p ; tm = False ; ba = False ; dt = False ; ns = False} ;
    To = ss "to" ; Me = ss "me" ; Pen = ss "pen" ; Din = ss "din" ; Wan = ss "wan" ; Yi = ss "yi" ;
    Bu = ss "bu" ; Sun = ss "sun" ; Go = ss "go" ; Nen = ss "nen" ; NenNen = ss ("nen" ++ "nen") ;
    Yen = ss "yen" ; Lu = ss "lu" ; Un = ss "un" ;

    -- 5.3: nothing inside a relative clause may be closed by a pause or kiyo (it would close the clause)
    RelSubj vp = case vp.p of {
      False => {s = "man" ++ vp.s ; e = ER ; p = False} ;
      True => {s = Predef.nonExist ; e = ER ; p = False}} ;
    RelObj np v = case pz np v.p of {
      False => {s = "man" ++ np.s ++ v.s ; e = ER ; p = False} ;
      True => {s = Predef.nonExist ; e = ER ; p = False}} ;
    RelPrep np v pr = case <pz np v.p, opn v.e> of {
      <False, False> => {s = "man" ++ np.s ++ v.s ++ pr.s ; e = ER ; p = False} ;
      _ => {s = Predef.nonExist ; e = ER ; p = False}} ;
    RelWhose q v = case pz q v.p of {
      False => {s = "man" ++ q.s ++ "pi" ++ ("wan" | "bu" | "wan" ++ "la") ++ v.s ; e = ER ; p = False} ;
      True => {s = Predef.nonExist ; e = ER ; p = False}} ;
    SlashV v = {s = v.s ; e = EV ; p = False} ;
    SlashV3 v r = {s = v.s ++ r.s ; e = r.e ; p = r.p} ;
    SlashTAM h a v = case <h.e, a.e> of {
      <True, True> => {s = Predef.nonExist ; e = EV ; p = False} ;
      _ => v ** {s = h.s ++ a.s ++ v.s}} ;
    SlashOp o v = v ** {s = o.s ++ v.s} ;
    SlashAdv v a = {s = seq v a.s ; e = a.e ; p = pz v a.p} ;

    Po = dg "po" True False False ; Fi = dg "fi" False True True ; Sa = dg "sa" False False True ;
    Ka = dg "ka" False False False ; Da = dg "da" False False False ; Te = dg "te" False False False ;
    Ufo = dg "ufo" False False False ; Oma = dg "oma" False False False ;
    Kefi = dg "kefi" False False False ; Mape = dg "mape" False False False ;
    Units d = {s = d.s ; z = d.z ; one = d.one ; hr = notB d.z} ;
    Tens d = case d.z of {
      False => {s = tens d ; z = False ; one = False ; hr = d.one} ;
      True => {s = Predef.nonExist ; z = False ; one = False ; hr = False}} ;
    TensU d u = case <d.z, u.z> of {
      <False, False> => {s = tens d ++ u.s ; z = False ; one = False ; hr = andB d.one u.small} ;
      _ => {s = Predef.nonExist ; z = False ; one = False ; hr = False}} ;
    S100 n = {s = n.s ; z = n.z ; one = n.one} ;
    Hund d = case d.z of {
      False => {s = hund d ; z = False ; one = False} ;
      True => {s = Predef.nonExist ; z = False ; one = False}} ;
    HundR d r = case <d.z, r.z> of {
      <False, False> => {s = hund d ++ r.s ; z = False ; one = False} ;
      _ => {s = Predef.nonExist ; z = False ; one = False}} ;
    S1000 n = ss n.s ;
    Thou n = case orB n.z n.one of {False => ss (n.s ++ "munno") ; True => ss Predef.nonExist} ;
    ThouR n r = case <orB n.z n.one, r.z> of {<False, False> => ss (n.s ++ "munno" ++ r.s) ; _ => ss Predef.nonExist} ;
    Thou1 = ss "munno" ;
    Thou1R r = case r.z of {False => ss ("munno" ++ r.s) ; True => ss Predef.nonExist} ;
    Decimal n d = ss (n.s ++ "mimi" ++ d.s) ;
    Dg1 d = {s = d.s ; n2 = False ; n3 = False} ;
    DgN ds d = {s = ds.s ++ d.s ; n2 = True ; n3 = ds.n2} ;
}
