#
# Collective Knowledge (individual environment - setup)
#
# See CK LICENSE.txt for licensing details
# See CK COPYRIGHT.txt for copyright details
#
# Developer: Grigori Fursin, Grigori.Fursin@cTuning.org, http://fursin.net
#

##############################################################################
# setup environment setup

def setup(i):
    """
    Input:  {
              cfg              - meta of this soft entry
              self_cfg         - meta of module soft
              ck_kernel        - import CK kernel module (to reuse functions)

              host_os_uoa      - host OS UOA
              host_os_uid      - host OS UID
              host_os_dict     - host OS meta
              
              target_os_uoa    - target OS UOA
              target_os_uid    - target OS UID
              target_os_dict   - target OS meta

              target_device_id - target device ID (if via ADB)

              tags             - list of tags used to search this entry

              env              - updated environment vars from meta
              customize        - updated customize vars from meta

              deps             - resolved dependencies for this soft

              interactive      - if 'yes', can ask questions, otherwise quiet
            }

    Output: {
              return       - return code =  0, if successful
                                         >  0, if error
              (error)      - error text if return > 0

              bat          - prepared string for bat file
            }

    """

    import os

    # Get variables
    ck=i['ck_kernel']
    s=''

    iv=i.get('interactive','')

    env=i.get('env',{})
    cfg=i.get('cfg',{})
    deps=i.get('deps',{})
    tags=i.get('tags',[])
    cus=i.get('customize',{})

    host_d=i.get('host_os_dict',{})
    target_d=i.get('target_os_dict',{})
    winh=host_d.get('windows_base','')
    win=target_d.get('windows_base','')
    mingw=target_d.get('mingw','')
    tbits=target_d.get('bits','')

    envp=cus.get('env_prefix','')
    pi=cus.get('path_install','')

    fp=cus.get('full_path','')
    if fp!='':
       p1=os.path.dirname(fp)
       p2=os.path.dirname(p1)
       p3=os.path.dirname(p2)
       pi=os.path.dirname(p3)

    ep=cus.get('env_prefix','')
    if ep!='':
       if pi!='':
          env[ep]=pi

    ################################################################
    if win=='yes':
       if tbits=='64': 
          yy='Release\\x64'
       else: 
          yy='Release\\Win32'

       s+='set PATH='+pi+'\\bin\\'+yy+';%PATH%\n\n'

       cus['path_bin']=pi+'\\bin\\'+yy
       cus['path_lib']=pi+'\\lib\\'+yy
       cus['path_include']=pi+'\\include'

    else:
       return {'return':1, 'error':'Linux version is not yet supported'}

    return {'return':0, 'bat':s}
