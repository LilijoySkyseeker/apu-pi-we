# Family-balanced colexification rate from CLICS4 (2026-10-08, from research/notes/colexification.md).
# Input: CLICS4 colexifications table + languages.csv (CLDF). Rate = mean over families of the share
# of each family's languages that lump the pair; take the max per language (the table has a duplicate 0 row beside each 1).
# usage: gawk -v FPAT='([^,]*)|("[^"]*")' -f rates.awk pairs.txt colexifications.csv languages.csv values.csv
# Family-balanced colexification rate per CLICS4 pair. values.csv has duplicate 0/1 rows per language; take max.
NR==FNR{want[$0]=1; next}
FILENAME=="colexifications.csv"{ n2=$2; gsub(/^"|"$/,"",n2); if(FNR>1 && (n2 in want)) pid[$1]=n2; next}
FILENAME=="languages.csv"{ if(FNR>1){f=$9; if(f=="") f="iso_" $1; fam[$1]=f}; next}
{ split($0,a,","); p=a[3]; if(!(p in pid)) next; k=p SUBSEP a[2]; if(!(k in val) || a[4]>val[k]) val[k]=a[4] }
END{ for(k in val){split(k,b,SUBSEP); p=b[1]; v=val[k]; F=fam[b[2]]; n[p]++; s[p]+=v; fk=p SUBSEP F; fn[fk]++; fs[fk]+=v }
  for(k in fn){split(k,b,SUBSEP); p=b[1]; nf[p]++; frac[p]+=fs[k]/fn[k]; if(fs[k]>0) fp[p]++}
  for(p in pid) if(nf[p]) printf "%s\tvar %d/%d\tfam %d/%d\tfam-bal %.1f%%\n", pid[p], s[p], n[p], fp[p], nf[p], 100*frac[p]/nf[p] }
