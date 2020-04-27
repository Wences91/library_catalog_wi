from worldcatidentities import Authority, AuthorityData

def download_uris(uris):
    out_file_author = open('data/uri_worldcat_identities_author.tsv', 'w')
    out_file_author.write('author\tidentity\tlanguages\ttotal_holdings\twork_count\trecord_count\tauthor_id' + '\n')

    out_file_languages = open('data/uri_worldcat_identities_langs.tsv', 'w')
    out_file_languages.write('author\tauthor_id\tlang\tcount' + '\n')

    out_file_works = open('data/uri_worldcat_identities_works.tsv', 'w')
    out_file_works.write('author\tauthor_id\ttitle\tlang\tholdings\teditions\ttype' + '\n')
    
    for i in range(len(uris)):
        authority = AuthorityData(name=uris.loc[i, 'author'], uri=uris.loc[i, 'author_id']).data()
        if authority.finded:
            print('\r' + uris.loc[i, 'author'] + ' ' + authority.established_form + ' ' * (70 - 1 + len(uris.loc[i, 'author']) + len(authority.established_form)), end='\r')
            out_file_author.write('\t'.join([uris.loc[i, 'author'], authority.established_form, authority.languages_total, authority.total_holdings, authority.work_count, authority.record_count, authority.uri.split('/')[2]]) + '\n')
            for l in authority.languages:
                out_file_languages.write(authority.name + '\t' + '\t'.join([authority.uri.split('/')[2], l[0], l[1]]) + '\n')
            for w in authority.works:
                if w != '0': # 0 is for the header
                    out_file_works.write(authority.name + '\t' + authority.uri.split('/')[2] + '\t' + '\t'.join(authority.works[w]) + '\n')

    out_file_author.close()
    out_file_languages.close()
    out_file_works.close()
    
    print('\nDownload completed!')

