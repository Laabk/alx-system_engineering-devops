# this install the flask, version 2.1.0 from pip3 using puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
