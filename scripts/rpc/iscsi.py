from client import print_dict, print_array, int_arg


def get_luns(args):
    print_dict(args.client.call('get_luns'))


def get_portal_groups(args):
    print_dict(args.client.call('get_portal_groups'))


def get_initiator_groups(args):
    print_dict(args.client.call('get_initiator_groups'))


def get_target_nodes(args):
    print_dict(args.client.call('get_target_nodes'))


def construct_target_node(args):
    luns = []
    for u in args.bdev_name_id_pairs.strip().split(" "):
        bdev_name, lun_id = u.split(":")
        luns.append({"bdev_name": bdev_name, "lun_id": int(lun_id)})

    pg_ig_maps = []
    for u in args.pg_ig_mappings.strip().split(" "):
        pg, ig = u.split(":")
        pg_ig_maps.append({"pg_tag": int(pg), "ig_tag": int(ig)})

    params = {
        'name': args.name,
        'alias_name': args.alias_name,
        'pg_ig_maps': pg_ig_maps,
        'luns': luns,
        'queue_depth': args.queue_depth,
    }

    if args.chap_group:
        params['chap_group'] = args.chap_group
    if args.disable_chap:
        params['disable_chap'] = args.disable_chap
    if args.require_chap:
        params['require_chap'] = args.require_chap
    if args.mutual_chap:
        params['mutual_chap'] = args.mutual_chap
    if args.header_digest:
        params['header_digest'] = args.header_digest
    if args.data_digest:
        params['data_digest'] = args.data_digest
    args.client.call('construct_target_node', params)


def target_node_add_lun(args):
    params = {
        'name': args.name,
        'bdev_name': args.bdev_name,
    }
    if args.lun_id:
        params['lun_id'] = args.lun_id
    args.client.call('target_node_add_lun', params)


def delete_pg_ig_maps(args):
    pg_ig_maps = []
    for u in args.pg_ig_mappings.strip().split(" "):
        pg, ig = u.split(":")
        pg_ig_maps.append({"pg_tag": int(pg), "ig_tag": int(ig)})
    params = {
        'name': args.name,
        'pg_ig_maps': pg_ig_maps,
    }
    args.client.call('delete_pg_ig_maps', params)


def add_pg_ig_maps(args):
    pg_ig_maps = []
    for u in args.pg_ig_mappings.strip().split(" "):
        pg, ig = u.split(":")
        pg_ig_maps.append({"pg_tag": int(pg), "ig_tag": int(ig)})
    params = {
        'name': args.name,
        'pg_ig_maps': pg_ig_maps,
    }
    args.client.call('add_pg_ig_maps', params)


def add_portal_group(args):
    # parse out portal list host1:port1 host2:port2
    portals = []
    for p in args.portal_list:
        ip, separator, port_cpumask = p.rpartition(':')
        split_port_cpumask = port_cpumask.split('@')
        if len(split_port_cpumask) == 1:
            port = port_cpumask
            portals.append({'host': ip, 'port': port})
        else:
            port = split_port_cpumask[0]
            cpumask = split_port_cpumask[1]
            portals.append({'host': ip, 'port': port, 'cpumask': cpumask})

    params = {'tag': args.tag, 'portals': portals}
    args.client.call('add_portal_group', params)


def add_initiator_group(args):
    initiators = []
    netmasks = []
    for i in args.initiator_list.strip().split(' '):
        initiators.append(i)
    for n in args.netmask_list.strip().split(' '):
        netmasks.append(n)

    params = {'tag': args.tag, 'initiators': initiators, 'netmasks': netmasks}
    args.client.call('add_initiator_group', params)


def add_initiators_to_initiator_group(args):
    initiators = []
    netmasks = []
    if args.initiator_list:
        for i in args.initiator_list.strip().split(' '):
            initiators.append(i)
    if args.netmask_list:
        for n in args.netmask_list.strip().split(' '):
            netmasks.append(n)

    params = {'tag': args.tag, 'initiators': initiators, 'netmasks': netmasks}
    args.client.call('add_initiators_to_initiator_group', params)


def delete_initiators_from_initiator_group(args):
    initiators = []
    netmasks = []
    if args.initiator_list:
        for i in args.initiator_list.strip().split(' '):
            initiators.append(i)
    if args.netmask_list:
        for n in args.netmask_list.strip().split(' '):
            netmasks.append(n)

    params = {'tag': args.tag, 'initiators': initiators, 'netmasks': netmasks}
    args.client.call('delete_initiators_from_initiator_group', params)


def delete_target_node(args):
    params = {'name': args.target_node_name}
    args.client.call('delete_target_node', params)


def delete_portal_group(args):
    params = {'tag': args.tag}
    args.client.call('delete_portal_group', params)


def delete_initiator_group(args):
    params = {'tag': args.tag}
    args.client.call('delete_initiator_group', params)


def get_iscsi_connections(args):
    print_dict(args.client.call('get_iscsi_connections'))


def get_iscsi_global_params(args):
    print_dict(args.client.call('get_iscsi_global_params'))


def get_scsi_devices(args):
    print_dict(args.client.call('get_scsi_devices'))
