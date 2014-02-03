%define		  _enable_debug_packages %{nil}
%define           debug_package            %{nil}


%define           distsuffix mib
Vendor:           MIB - Mandriva Italia Backports - http://mib.pianetalinux.org/
Packager:         Francesco Mancuso <mcfrank@tiscali.it>

%if %mdkversion >= 201200
# rpmlint just sucks!!!
%define _build_pkgcheck_set %{nil}
%define _build_pkgcheck_srpm %{nil}
%endif

%define rel	266.69.3

%define svn	0
%define pre	0

%if %svn
%define release		%mkrel 1.%svn.%rel
# define distname	%{svn}-%{name}_dev.tar.bz2
#20090507-aMule-AdunanzA_dev.tar.bz2

#define distname aMule-AdunanzA-MrHyde-r168-svn20090613.tar.bz2

%define dirname		%name
%else
%if %pre
%define release		%mkrel 0.%pre.%rel
%define distname	%name-%version.%pre.tar.bz2
%define dirname		%name-%version.%pre
%else
%define release		%mkrel %rel
%define distname	aMule-AdunanzA-2010.1-2.2.6.tar.bz2
#%name-%version.tar.bz2
%define dirname		%name-%version
%endif
%endif

%define release %mkrel %rel

%define oname aMule-AdunanzA
%define iname amule
%define zname amule-adunanza
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}


Summary: File sharing client compatible with eDonkey
Name:		amule-adunanza
Version:	2010.1
Release:	%{release}
License: GPL
Group: Networking/File transfer

#Source:  http://ovh.dl.sourceforge.net/sourceforge/amule/%{oname}-%version.tar.bz2
#Source:	  /usr/src/rpm/SOURCES/aMule-AdunanzA-%version.tar.bz2

Source0:	  /usr/src/rpm/SOURCES/%{distname}

# aMule-AdunanzA-current-%version-%cvs_date.tar.bz2
Source10: amule-16.png
Source11: amule-32.png
Source12: amule-48.png
Source13: amule.png

Patch0:	wxcasframe.patch
Patch1: amule-adunanza-wxdef.patch

URL: http://amule.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-buildroot

BuildRequires: Vgd-devel) >= 2.0
BuildRequires: pkgconfig(curl)
BuildRequires: png-devel
BuildRequires: pkgconfig(cryptopp)
BuildRequires: pkgconfig(ncurses)
#BuildRequires: pkgconfig(readline)
BuildRequires: pkgconfig(gettext)
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(wxgtku) >= 2.8.12
BuildRequires: cvs
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(binutils)
BuildRequires: pkgconfig(libupnp)
BuildRequires: pkgconfig(GeoIP)
BuildRequires: pkgconfig(gtk2)
BuildRequires: pkgconfig(glib)

# libwxgtku2.8-devel
BuildRequires: automake1.7

Conflicts: xmule < 1.6.0-2plf
# added by mcfrank
Conflicts:	aMule-AdunanzA
Conflicts: amule <= 2.2.2-20081004.1.2plf
Obsoletes: amule <= 2.2.2-20081004.1.2plf
Obsoletes: amule

Summary: File sharing client compatible with eDonkey
Group: Networking/File transfer
#Requires: amule

%description
aMule is an easy to use multi-platform client for ED2K Peer-to-Peer
Network.  It is a fork of xMule, whis was based on emule for
Windows. aMule currently supports (but is not limited to) the
following platforms: Linux, *BSD and MacOS X.

#This package is in PLF because Mandriva does not allow P2P softwares

#Provides: alc amule amulegui cas ed2k-amule wxcas
#Obsoletes: amule1



%package commandline
Summary: File sharing client compatible with eDonkey
Group: Networking/File transfer
#Requires: amule
Requires: %zname
# added by mcfrank
Conflicts:	aMule-AdunanzA

%description commandline
aMule is an easy to use multi-platform client for ED2K Peer-to-Peer
Network.  It is a fork of xMule, whis was based on emule for
Windows. aMule currently supports (but is not limited to) the
following platforms: Linux, *BSD and MacOS X.

This is the command line tool to control aMule remotely (or locally:).

aMule is in PLF because Mandriva does not allow P2P softwares

#Provides: alcc amulecmd amuled
#Obsoletes: amule1



%package webserver
Summary: File sharing client compatible with eDonkey
Group: Networking/File transfer
#Requires: amule
Requires: %zname
# added by mcfrank
Conflicts:	aMule-AdunanzA

%description webserver
aMule is an easy to use multi-platform client for ED2K Peer-to-Peer
Network.  It is a fork of xMule, whis was based on emule for
Windows. aMule currently supports (but is not limited to) the
following platforms: Linux, *BSD and MacOS X.

This is the webserver to control aMule remotely (or locally:).

aMule is in PLF because Mandriva does not allow P2P softwares

#Provides: amuleweb
#Obsoletes: amule1



%prep
rm -rf %buildroot
%setup -q -n %oname-2010.1-2.2.6
#MrHyde-r168-svn20090613
#-%version
%patch0 -p1 -b .frame
%patch1 -p1 -b .wxdef

%build
%configure2_5x \
--with-wx-config=%{_bindir}/wx-config-unicode\
               --enable-ccache\
               --enable-optimize\
               --enable-runtime-cpudetection\
               --enable-amule-daemon\
               --enable-amulecmd\
               --enable-amulecmdgui\
               --enable-amule-gui \
               --enable-webserver\
               --enable-webservergui\
               --enable-gsocket\
               --enable-cas\
               --enable-wxcas\
               --enable-alc\
               --enable-alcc \
               --enable-embedded_crypto\
               --disable-debug\
               --enable-utf8-systray\
               --enable-amule-daemon\
               --enable-kad-compile\
               --enable-systray\
               --enable-skins\
               --enable-geoip\
               --enable-unpnp\
               --disable-rpath\


%make

%install


%makeinstall
rm -rf %{buildroot}%{_datadir}/locale/ee/LC_MESSAGES/amule.mo
%find_lang %{oname}

install -m 644 -D %{SOURCE10} %{buildroot}%{_miconsdir}/amule-16.png
install -m 644 -D %{SOURCE11} %{buildroot}%{_iconsdir}/amule-32.png
install -m 644 -D %{SOURCE12} %{buildroot}%{_liconsdir}/amule-48.png
install -m 644 -D %{SOURCE13} %{buildroot}%{_iconsdir}/amule.png

mkdir -p %{buildroot}%{_menudir}

# Fix wrong-script-end-of-line-encoding
perl -pi -e 's/\015$//' %buildroot/%_datadir/doc/amuleadunanza/amule-win32.HOWTO.txt


rm -f %buildroot/%_datadir/doc/amule-%{version}/man/.cvsignore

#Menu
#cat > %{buildroot}%{_menudir}/%{name} <<EOF
#?package(%name): needs="x11" \
#%if %mdkversion < 1000 
#section="Networking/File transfer" \
#%else 
#section="Internet/File Transfer" \
#%endif
#title="aMule Adunanza" longtitle="File sharing client compatible with eDonkey" command="amule" icon="%{name}.png" #xdg="true"
#EOF


#cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
cat > %{buildroot}%{_menudir}/%{oname} <<EOF
[Desktop Entry]
Encoding=UTF-8

# for menu
%define title	aMule AdunanzA
%define comment	File sharing client compatible with eDonkey

# menu
Name=%{title}
Comment=%{comment}
Exec=%{_bindir}/%{oname}
Icon=/usr/share/icons/amule.png
Terminal=false
Type=Application
Categories=GTK;Network;FileTransfer;P2P;X-MandrivaLinux-CrossDesktop;
EOF

desktop-file-install --vendor="" \
  --add-category="GTK" \
  --add-category="FileTransfer" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


mv %buildroot%_bindir/ed2k %buildroot%_bindir/ed2k-%oname
#rm -rf %buildroot%_datadir/doc/%name-%version
rm -rf %buildroot%_datadir/doc/%oname-%version
rm -f %buildroot/%{_libdir}/xchat/plugins/xas.pl
cat > $RPM_BUILD_DIR/%oname-2010.1-2.2.6/README.Debian-Packages << EOF
#cat > $RPM_BUILD_DIR/%oname-MrHyde-r168-svn20090613/README.update.urpmi << EOF
WARNING :
aMule may segfault after an upgrade from 1.2.x to this version.
In this case, just rename the ".aMule" directory in your home as, say,
".aMule-1.2". It may even keep the preferences !!
Hum, well, that's just a "it works for me" (tm) trick (maybe it used the 
config in ".xMule"? 
If necessary, reconfigure aMule, of course. 

ATTENTION : 
aMule peut ne pas fonctionner aprös une mise ö jour de 1.2.x ö cette version 
Dans ce cas, pas de panique ! Renommez le dossier ".aMule" ö la racine de 
votre röpertoire utilisateur en ".aMule-1.2". 
Cela peut möme conserver les pröförences !! 
Enfin "öa marche chez moi" (tm) (peut-ötre gröce au dossier ".xMule" qui 
trainait lö aussi!) 
Si nöcessaire, reconfigurez aMule. 

ACHTUNG :
aMule könnte bei einer Aktualisierung von Version 1.2 auf diese Version
abstörzen. Wenn dies auftritt benenne .aMule in z.B. .aMule-1.2 um. Es kann
sogar sein, das die Einstellungen beibehalten werden. Dies ist aber nur ein
Trick welcher för mich funktioniert hat (Vielleicht kamen die Einstellungen
auch aus dem Verzeichnis .xMule.
Wenn nötig, musst du aMule natörlich neu konfigurieren.

ATTENZIONE :
aMule può dare errore di segfault dopo un aggiornamento da 1.2.x a questa versione.
In questo caso, occorre solo rinominare la directory ".aMule"  nella vostra /home/guest
dove guest può essere o il vostro nome o altro, rinominatelo in,".aMule-1.2".
Questo può anche mantenere le preferenze !!
Si, bene, "fare questo per me va" (tm) trick (può darsi che sia usata la config in ".xMule"? 
Altrimenti se occorre, riconfigurate aMule. :)
EOF

%clean
rm -rf %buildroot

%post
%{update_menus}
update-alternatives --install %{_bindir}/ed2k ed2k %{_bindir}/ed2k-%iname 5

%postun
%{clean_menus}
update-alternatives --remove ed2k %{_bindir}/ed2k-%iname


%files 
%defattr(-,root,root)
%{_bindir}/amule
%{_bindir}/autostart-xas
%_bindir/amulegui
%{_bindir}/wxcas
%{_bindir}/cas
#%{_bindir}/ed2k
%{_bindir}/alc
%{_libdir}/xchat/plugins/*
%{_datadir}/amuleadunanza/skins/*
%{_datadir}/applications/alcadunanza.desktop
%{_datadir}/applications/amuleadunanza.desktop
%{_datadir}/applications/amuleguiadunanza.desktop
%{_datadir}/applications/wxcasadunanza.desktop
%{_datadir}/casAdunanzA/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(eu) %{_mandir}/eu/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(fr) %{_mandir}/fr/man1/*
# added by mcfrank
%{_mandir}/it/man1/*
#
%{_mandir}/man1/*
%{_docdir}/amuleadunanza/*
%{_datadir}/locale/it/LC_MESSAGES/amuleadunanza.mo
%{_datadir}/pixmaps/alcadunanza.xpm
%{_datadir}/pixmaps/amuleadunanza.xpm
%{_datadir}/pixmaps/amuleguiadunanza.xpm
%{_datadir}/pixmaps/wxcasadunanza.xpm
# added by mcfrank
%{_miconsdir}/%{iname}-16.png
%{_iconsdir}/%{iname}-32.png
%{_liconsdir}/%{iname}-48.png
%{_iconsdir}/%{iname}.png
%{_bindir}/ed2k-%oname
%ifarch x86_64
/usr/lib/menu/%oname
%else
%{_libdir}/menu/%oname
%endif


%files commandline
%defattr(-,root,root)
%doc docs/README
%{_bindir}/amulecmd
%{_bindir}/alcc
%_bindir/amuled



%files webserver
%defattr(-,root,root)
%doc docs/README
%{_bindir}/amuleweb
%{_datadir}/amuleadunanza/webserver/*

%define date	%(echo `LC_ALL="C" date +"%a %b %d %Y"`)
%changelog
* Sun Feb 02 2014 Francesco Mancuso <mcfrank@tiscali.it>  2.6.6.69.3mib2012.1
+ Version 2010.1-2.2.6
- rebuild vs new wx
- MIB (Mandriva International Backport) - http://mib.pianetalinux.org/

* Sat Oct 14 2011 Francesco Mancuso <mcfrank@tiscali.it>  2.6.6.69.3mib2011
+ Version 2010.1-2.2.6
- rebuild vs new wx
- MIB (Mandriva International Backport) - http://mib.pianetalinux.org/

* Wed Oct 12 2011 Francesco Mancuso <mcfrank@tiscali.it>  2.6.6.69.2mib2011
+ Version 2010.1-2.2.6
- rebuild for fixing requires on 2011.
- added patch0 4 build on 2011
- added patch1 by Pulfer to fix build
- MIB (Mandriva International Backport) - http://mib.pianetalinux.org/

* Sun Oct 24 2010 Francesco Mancuso <mcfrank@tiscali.it>  2.6.6.69.1mib
+ Version 2010.1-2.2.6
- MIB (Mandriva International Backport) - http://mib.pianetalinux.org/

* Mon Mar 01 2010 Francesco Mancuso <mcfrank@tiscali.it>  3.14b3-2.6.6.69.1mib
+ Version 3.14b3-2.6.6
- MIB (Mandriva International Backport) - http://mib.pianetalinux.org/

* Fri Jun 19 2009 Francesco Mancuso <mcfrank@tiscali.it>  3.14b4-svn20090613-69.1mib
+ Version 3.14b4-svn20090613
- Updated with new GeoIP.dat May 01  2009 by mcfrank
- With new geoip-1.4.6
- svn from MrHyde
- MIB (Mandriva Italia Backport) new optimized full port release.

* Fri May 08 2009 Francesco Mancuso <mcfrank@tiscali.it>  3.14b4-svn20090519-69.1mib
+ Version 3.14b4-svn20090519
- Updated with new GeoIP.dat May 01  2009 by mcfrank
- With new geoip-1.4.6
- svn from MrHyde
- MIB (Mandriva Italia Backport) new optimized full port release.

* Fri May 08 2009 Francesco Mancuso <mcfrank@tiscali.it>  3.14b4-cvs20080930-69.1mib
+ Version 3.14b4-svn20090507
- Updated with new GeoIP.dat May 01  2009 by mcfrank
- With new geoip-1.4.6
- svn from MrHyde
- MIB (Mandriva Italia Backport) new optimized full port release.

* Sun Oct 05 2008 Francesco Mancuso <mcfrank@tiscali.it>  3.14b3-cvs20080930-69.1plf.mib2008.1
+ Version 3.14b3-cvs20080930
- Updated with new GeoIP.dat Oct 03  2008 by mcfrank
- With --disable-debug activated
- With new libupnp 1.6.6
- MIB (Mandriva Italia Backport) new optimized full port release.

* Sun Oct 05 2008 Francesco Mancuso <mcfrank@tiscali.it>  3.14b3-cvs20080030-69.1plf.mib2007.1
+ Version 3.14b3-cvs20080930
- Updated with new GeoIP.dat Oct 03 2008 by mcfrank
- With --disable-debug activated
- With new libupnp 1.6.6
- MIB (Mandriva Italia Backport) new optimized full port release.

* Sun May 25 2008 Francesco Mancuso <mcfrank@tiscali.it>  3.14b2-cvs20080430-1.1plf.mib2008.1
+ Version 3.14b2 - CVS 20080430
- Updated with new GeoIP.dat May 01 2008 by mcfrank
- With --enable-debug activated
- MIB (Mandriva Italia Backport) new optimized full port release.

* Sun May 25 2008 Francesco Mancuso <mcfrank@tiscali.it>  3.14b2-cvs20080430-1.1plf.mib2007.1
+ Version 3.14b2 - CVS 20080430
- Updated with new GeoIP.dat May 01 2008 by mcfrank
- With --enable-debug activated
- MIB (Mandriva Italia Backport) new optimized full port release.

* Fri Mar 14 2008 Francesco Mancuso <mcfrank@tiscali.it>  3.14b1-cvs20080304-1.1plf.mib2007.1
+ Version 3.14b1 - CVS 20080304
- Updated with new GeoIP.dat March 05 2008 by mcfrank
- With --enable-debug activated
- MIB (Mandriva Italia Backport) new optimized full port release.

* Fri Mar 07 2008 Francesco Mancuso <mcfrank@tiscali.it>  3.14b1-cvs20080203-1.2plf.mib2007.1
+ Version 3.14b1 - CVS 20080203
- Updated with new GeoIP.dat March 05 2008 by mcfrank
- With --enable-debug activated
- MIB (Mandriva Italia Backport) new optimized full port release.

* Mon Jan 21 2008 Francesco Mancuso <mcfrank@tiscali.it>  3.14b1-cvs20080109.1.2plf.mib2007.1
+ Version 3.14b1 - CVS 20080109
- Prepared with every possible features just enabled out of the box...
- For others optimizations/integrations, optimized compiler platform:
- Rebuilt with new libcryptopp-5.5.2-1.2 (thanks to mcfrank@tiscali.it)
- Rebuilt now with new Libupnp0-1.6.3.1.1mib for better Port Forwarding
- Rebuilt now with new GeoIP-1.4.3-2.1.mib with dbase upd to 2008.01.01
- MIB (Mandriva Italia Backport) new optimized fullport release.

* Fri Jan 18 2008 Nicolo' Costanza <abitrules@yahoo.it> 3.14b1-cvs20080109-1.2plf.mib2008.0
+ Version 3.14b1 - CVS 20080109
- Prepared with every possible features just enabled out of the box...
- For others optimizations/integrations, optimized compiler platform:
- Rebuilt with new libcryptopp-5.5.2-1.2 (thanks to mcfrank@tiscali.it)
- Rebuilt now with new Libupnp0-1.6.3.1.1mib for better Port Forwarding
- Rebuilt now with new GeoIP-1.4.3-2.1.mib with dbase upd to 2008.01.01
- MIB (Mandriva Italia Backport) new optimized fullport release.

* Wed Jan 16 2008 Francesco Mancuso <mcfrank@tiscali.it>  3.14b1-cvs20080109.1.1mib2007.1
+ Version 3.14b1
- With every possible features just enabled out of the box
- MIB (Mandriva Italia Backport) new optimized full port release.

* Wed Jan 16 2008 Nicolo' Costanza <abitrules@yahoo.it> 3.14b1-cvs20080109-1.1plf.mib2008.0
+ Version 3.14b1 - CVS 20080109
- Prepared with every possible features just enabled out of the box
- MIB (Mandriva Italia Backport) new optimized fullport release.