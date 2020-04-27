from worldcatidentities import Authority, AuthorityData

def download_names(file):
    with open('data/' + file, 'r') as file:
        rows = []
        for row in file:
            row = row.rstrip()
            rows.append(row)


    out_file_author = open('data/worldcat_identities_author.tsv', 'w')
    out_file_author.write('author\tidentity\tlanguages\ttotal_holdings\twork_count\trecord_count\tauthor_id' + '\n')

    out_file_languages = open('data/worldcat_identities_langs.tsv', 'w')
    out_file_languages.write('author_id\tlang\tcount' + '\n')

    out_file_works = open('data/worldcat_identities_works.tsv', 'w')
    out_file_works.write('author_id\ttitle\tlang\tholdings\teditions\ttype' + '\n')
    
    for author in rows:
        authority = AuthorityData(name=author).data()
        if authority.finded:
            print('\r' + author + ' ' + authority.established_form + ' ' * (70 - 1 + len(author) + len(authority.established_form)), end='\r')
            out_file_author.write('\t'.join([author, authority.established_form, authority.languages_total, authority.total_holdings, authority.work_count, authority.record_count, authority.uri.split('/')[2]]) + '\n')
            for l in authority.languages:
                out_file_languages.write('\t'.join([authority.uri.split('/')[2], l[0], l[1]]) + '\n')
            for w in authority.works:
                if w != '0': # 0 is for the header
                    out_file_works.write(authority.uri.split('/')[2] + '\t' + '\t'.join(authority.works[w]) + '\n')

    out_file_author.close()
    out_file_languages.close()
    out_file_works.close()
    
    print('\nDownload completed!')
