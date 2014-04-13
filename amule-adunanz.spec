%define debug_package	%{nil}
%define oname aMule-AdunanzA


Summary:        File sharing client compatible with eDonkey
Name:		amule-adunanza
Version:	2012.1
Release:	2.3.1
License:        GPL
Group:          Networking/File transfer
URL:            http://amule.sourceforge.net
Source0:	http://downloads.sourceforge.net/amule-adunanza/aMule-AdunanzA/Stable/%{oname}-%{version}-%{release}.tar.bz2


BuildRequires: gd-devel >= 2.0
BuildRequires: pkgconfig(libcurl)
BuildRequires: libcryptopp-devel
BuildRequires: pkgconfig(ncurses)
BuildRequires: gettext-devel
BuildRequires: desktop-file-utils
BuildRequires: wxgtku2.8-devel
BuildRequires: cvs
BuildRequires: pkgconfig(zlib)
BuildRequires: binutils-devel
BuildRequires: pkgconfig(libupnp)
BuildRequires: pkgconfig(gdk-2.0)
BuildRequires: pkgconfig(glib)
BuildRequires: automake1.7

Conflicts: xmule 
Conflicts: amule 
Obsoletes: amule

Suggests: xchat


%description
aMule is an easy to use multi-platform client for ED2K Peer-to-Peer
Network.  It is a fork of xMule, whis was based on emule for
Windows. aMule currently supports (but is not limited to) the
following platforms: Linux, *BSD and MacOS X.




%prep
%setup -qn %oname-%{version}-%{release}

%build
  ./configure --prefix=/usr \
  --with-wx-config=/usr/bin/wx-config \
  --mandir=/usr/share/man \
  --disable-upnp \
  --disable-debug \
  --enable-optimize

%make

%install
%makeinstall

%files 
%{_bindir}/*
%{_datadir}/amuleadunanza/skins/*
%{_datadir}/applications/*.desktop
%{_mandir}/*/man1/*
%{_mandir}/man1/*.1.xz
%{_docdir}/amuleadunanza/*
%lang (it) %{_datadir}/locale/it/LC_MESSAGES/amuleadunanza.mo
%lang (uk) %{_datadir}/locale/uk/LC_MESSAGES/amuleadunanza.mo
%{_datadir}/pixmaps/amuleadunanza.xpm



